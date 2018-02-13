def agrupa_dataframes(lista_variaveis, lista_dias, lista_mesref, keys, path):

    d = {}

#     lista_variaveis = ['VL_GARANTIA','VL_MERCADO','QTD_GAR'] # adicionar outras variaveis ...
#     lista_dias = ['02','07','30','60','90'] # adicionar outras referencias ...
#     lista_mesref = [201712, 201801] # adicionar outras referencias ... 
#     keys = ['NO_CPF_CGC','date']

    print('dataframes gerados na seguinte ordem ...')
    print('')
    for i in range(len(lista_variaveis)):
        for j in range(len(lista_dias)):
            for k in range(len(lista_mesref)):
                try:
                    d['df_'+
                      str(lista_variaveis[i])+'_'+
                      str(lista_dias[j])+'_'+
                      str(lista_mesref[k])] = (pd.read_pickle
                                               ((str(path)+'df_')+
                                                 str(lista_variaveis[i])+'_'+
                                                 str(lista_dias[j])+'_'+
                                                 str(lista_mesref[k])))
                except IOError:
                    0

                #checar ordem de geracao das bases 
                print('df_'+str(lista_variaveis[i])+'_'+str(lista_dias[j])+'_'+str(lista_mesref[k]))

    print('fim da geracao ...')
    print('')
    %time
    print('iniciando agrupamento por grupos distintos ...')
    d2 = {}
    for j in range(len(lista_mesref)):
        dfs = []
        for i in range(len(d.keys())):
            if d.keys()[i][-6:] == str(lista_mesref[j]):
    #             print(d.keys()[i])
                dfs.append((d[d.keys()[i]]))
    #             print(len(dfs))
        d2['df_full_'+str(lista_mesref[j])] = reduce(lambda left,right: pd.merge(left,right,how='outer',on=keys), dfs)
        
    %time
    print('fim do agrupamento!')
    
    return d2
