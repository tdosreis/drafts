def contagem_distinta_generalizada(df_original,indice,coluna,vl_base_origem,delta_t,n_cols,nova_variavel):

    # df_original = r
    # coluna = 'CPF'
    # indice = 'date2'

    from datetime import date
    lista_coluna = df_original[(coluna)].unique() # coluna pode ser CPF, COD_INTERM, CD_FIPE, etc...

    d0 = date(df_original[(indice)].min().year,df_original[(indice)].min().month,df_original[(indice)].min().day)
    d1 = date(df_original[(indice)].max().year,df_original[(indice)].max().month,df_original[(indice)].max().day)
    delta = d1-d0

    timeline = pd.date_range(d0.strftime('%Y-%m-%d'),periods=(delta.days+1),freq='D')

    df_total = pd.DataFrame(np.nan, index=timeline, columns=lista_coluna.tolist())

    df_total.index.name = (indice)
    df_total.columns.name = (coluna)

    df_total.reset_index(inplace=True)
    df_total = pd.melt(df_total, id_vars=[(indice)],var_name=(coluna), value_name='nan')
    df_total.drop(['nan'],axis=1,inplace=True)

    df_total = pd.merge(df_total,df_original,on=[(coluna),(indice)],how='left')

    matrix = df_total.pivot(index=(indice),columns=(coluna),values=(vl_base_origem)).values

    QTD_m = np.zeros((len(matrix[:,0]),(len(matrix[0,:]))))

    # delta_t = 10
    # ncols = 49

    for ii in range(n_cols):
        for i in range(len(matrix[:,ii])):
            if i < delta_t:
                b = []
                for j in range(len(matrix[:,ii][0:i])):
                    if type(matrix[:,ii][0:i][j]) == list:
                        for k in range(len(matrix[:,ii][0:i][j])):
                            b.append(matrix[:,ii][0:i][j][k])
                    else:
                        b.append(matrix[:,ii][0:i][j])

                QTD_m[i,ii] = np.count_nonzero(~np.isnan((list(set(b)))))

            elif i >= delta_t:
                b = []
                for j in range(len(matrix[:,ii][(i-delta_t):i])):
                    if type(matrix[:,ii][(i-delta_t):i][j]) == list:
                        for k in range(len(matrix[:,ii][(i-delta_t):i][j])):
                            b.append(matrix[:,ii][(i-delta_t):i][j][k])
                    else:
                        b.append(matrix[:,ii][(i-delta_t):i][j])

                QTD_m[i,ii] = np.count_nonzero(~np.isnan((list(set(b)))))

    # 5) Restaura DataFrame a partir das matrizes de teste # 
    ########################################################

    df_new = (((pd.DataFrame(data=QTD_m[:,:n_cols],index=timeline,columns=(lista_coluna.tolist()[:n_cols])))
               .stack()).reset_index()).rename(columns={'level_0': (indice), 'level_1': (coluna),0:(nova_variavel)})
    
    return df_new
