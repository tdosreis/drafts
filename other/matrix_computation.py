### Função para geração da matriz de score e variável de output do score ###
############################################################################
 
def matriz_de_rating(x,y,x_row,y_col,matrix,target,x_axis,y_axis):
 
    n = len(x)*len(y)  # numero de celulas da matriz de cruzamento
 
    ## Cria todas as condições de combinações possíveis
    k = 0
    conditions = ([0]*n)
#     print('combinações')
    for i in range(len(x)):
        for j in range(len(y)):
#             print(x[i],y[j])
            conditions[k] = (x_row == x[i]) & (y_col == y[j])  # ------>>>> correto
            k+=1         #Nota: importante manter ordenação X,Y dentro do loop de condições!!!
                         #(...pensando em uma estrutura matricial...)
#             print('condições...')
#             print(conditions) 
    
    nrows = len(matrix)
    ncols = len(matrix[0])
    lin_matrix_row = [0]*ncols*nrows
    lin_matrix_col = [0]*ncols*nrows
 
    k = 0
    for i in range(nrows):
        for j in range(ncols):
            lin_matrix_row[k] = np.array(matrix)[i][j]
            k+=1
 
    k = 0
    for i in range(ncols):
        for j in range(nrows):
            lin_matrix_col[k] = np.array(matrix)[:,i][j]
            k+=1
       
    df[target] = np.select(conditions,np.array(lin_matrix_col),default=0.0)
 
    array = [[np.nan]*len(x)]*len(y)
    index_x = 0
    k_index = 0
    for index_x in range(index_x,len(lin_matrix_row),len(x)):
        array[k_index] = lin_matrix_row[index_x:index_x+(len(x))]
        k_index +=1
 
    index = [0]*len(y)
    for i in range(len(y)):
        index[i] = str(y[i])
       
    columns = [0]*len(x)
    for j in range(len(x)):
        columns[j] = str(x[j])
     
    df_cm = pd.DataFrame(array, index, columns)
       
#     df_cm = pd.DataFrame(array, index = [i for i in (''.join(str(e) for e in list(map(int, y))))],
#                          columns = [i for i in (''.join(str(e) for e in list(map(int, x))))])
 
    plt.figure(figsize = (x_axis,y_axis))
    plt.title('Matriz de Rating')
 
    grafico = sns.heatmap(df_cm, annot=True, cmap='coolwarm')
   
    return grafico#, array, df
