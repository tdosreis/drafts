def media_movel_ajustada(df_original,indice,coluna,vl_base_origem,delta_t,n_cols,nova_variavel):
 
    lista_coluna = df_original[(coluna)].unique() # coluna pode ser CPF, COD_INTERM, CD_FIPE, etc...
    
    from datetime import date
    d0 = date(df_original[(indice)].min().year,df_original[(indice)].min().month,df_original[(indice)].min().day)
    d1 = date(df_original[(indice)].max().year,df_original[(indice)].max().month,df_original[(indice)].max().day)
    delta = d1-d0
    # print(delta.days)
    
    # 0) Cria escala de tempo ---> resolução mínima, dias ('D')
    timeline = pd.date_range(d0.strftime('%Y-%m-%d'),periods=(delta.days+1),freq='D')
    
    # 1) Define DataFrame generalizado (esqueleto) --->> necessário para garantir todos os pontos
    df_total = pd.DataFrame(np.nan, index=timeline, columns=lista_coluna.tolist())

    df_total.index.name = (indice)
    df_total.columns.name = (coluna)

    df_total.reset_index(inplace=True)
    df_total = pd.melt(df_total, id_vars=[(indice)],var_name=(coluna), value_name='nan')
    df_total.drop(['nan'],axis=1,inplace=True)

    # 2) Insere variáveis originais no DataFrame 'empty'
    df_total = pd.merge(df_total,df_original,on=[(coluna),(indice)],how='left')

    # 3) Gera matriz transposta a partir da base total original 
    matrix = scipy.sparse.csr_matrix((df_total.pivot(index=(indice),columns=(coluna),values=(vl_base_origem))).values).toarray()
    
    ## Corrige primeiro valor da matriz de deltas
    for j in range(len(matrix[0,:])):
        matrix[:,j][pd.Series(matrix[:,j]).first_valid_index()] = np.nan
    
    # 4) Criação da função generalizada de média por janela de tempo (backwards) 
    ###############################################################################

    VL_m = np.zeros((len(matrix[:,0]),(len(matrix[0,:]))))
    for j in range(n_cols):
        for i in range(len(matrix[:,0])):
            if i<delta_t:
                VL_m[i,j] = matrix[0:i,j][~np.isnan(matrix[0:i,j])].mean()
            elif i>=delta_t:
                VL_m[i,j] = matrix[(i-delta_t):i,j][~np.isnan(matrix[(i-delta_t):i,j])].mean()

#     QTD_m = np.zeros((len(matrix[:,0]),(len(matrix[0,:]))))
#     for j in range(n_cols):
#         for i in range(len(matrix[:,0])):
#             if i<delta_t:
#                 QTD_m[i,j] = (matrix[0:i,j][~np.isnan(matrix[0:i,j])]).sum()  # contar elementos anteriores ao ponto de marcação
#             elif i>=delta_t:
#                 QTD_m[i,j] = (matrix[(i-delta_t):i,j][~np.isnan(matrix[(i-delta_t):i,j])]).sum() # contar elementos anterior a t_0
            
    # 5) Restaura DataFrame a partir das matrizes de teste # 
    ########################################################

    df_new = (((pd.DataFrame(data=VL_m[:,:n_cols],index=timeline,columns=(lista_coluna.tolist()[:n_cols])))
               .stack()).reset_index()).rename(columns={'level_0': (indice), 'level_1': (coluna),0:(nova_variavel)})

    # 5) 'left join' na base original de comparacao # 
    #################################################
    #df_total = pd.merge(df_total,df_new,how='left',on=[(coluna),(indice)]) # ======> realizar 'merge' depois ...
    
    return df_new#, df_total, coluna, indice
