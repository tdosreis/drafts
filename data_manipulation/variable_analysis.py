# extracted from Jupyter notebook
 
%%time
 
print('criando base categorica do tipo 2: target encoder')
print()
 
from category_encoders import TargetEncoder
 
y = df_default.perf_bad60_m6
X = df_target_encoding
 
# use binary encoding to encode two categorical features
enc = TargetEncoder(cols=list(tipo_2_ajust)).fit(X, y)
 
# transform the dataset
numeric_dataset = enc.transform(X)
 
 
%%time
 
# variaveis continuas
print('criando base de variaveis continuas: flag de missing')
print()
 
refs = [('scr_ncc','scr_ncc_score'),
        ('scr_cc','scr_cc_SCORE'),
        ('cartao_ncc','cartao_ncc_ALIGNED_SCORE_01'),
        ('rating_pf','rating_pf_OSC_FINAL_SCORE1'),
        ('finan','finan_vl_risco_total'),
        ('bhv_pf','bhv_pf_score_final')]
 
dfs = {}
 
for ref in refs:
    %time
    print(ref[0])
    print()
    subgrupo = [s for s in df_continuum.columns.values if ref[0] in s]
    dfs[str(ref[0])] = df_continuum.loc[:,df_continuum.columns.isin(subgrupo)]
 
for ref in refs:
    dfs[ref[0]].loc[(dfs[ref[0]][ref[1]].isnull()==True),str(ref[0])+'_fl_missing'] = 1
    dfs[ref[0]].loc[(dfs[ref[0]][ref[1]].isnull()==False),str(ref[0])+'_fl_missing'] = 0
   
for ref in refs:
    dfs[ref[0]] = dfs[ref[0]].fillna(0)
   
lista_dfs = []   
for ref in refs:
    lista_dfs.append(dfs[ref[0]])
            
df_continuas = pd.concat([df for df in lista_dfs], axis=1)
 
filtro = [item for item in df_continuum.columns.values if item not in df_continuas.columns.values]
 
df_continuas = pd.concat([df_continuum.loc[:,df_continuum.columns.isin(filtro)],df_continuas],axis=1)
 
 
def parametros_da_base(df):
 
    description = df.describe(include='all')
   
    print('quantidade de variaveis por criterio de analise:')
    print('')
    ### Desvio padrão == 0; variáveis com único valor preenchido e sem NaN
    print('std = 0 s/ NaN:',
          df.loc[:,(list(description.loc['std',:] == 0)) & (description.loc['count',:]==df.shape[0])].shape[1])
    ### Desvio padrão ==0; variáveis com um único valor preenchido e COM NaN
    print('std = 0 c/ NaN:',
          df.loc[:,(list(description.loc['std',:] == 0)) & (description.loc['count',:]!=df.shape[0])].shape[1])
    ### Variáveis com todas observações com valores NaN
    print('std = 0, demais casos (avaliar):',
          df.loc[:,(list(description.loc['std',:].isnull())) & (description.loc['count',:]!=df.shape[0])].shape[1])
    print('variaveis restantes:',
          df.loc[:,list((description.loc['std',:] != 0) & (~description.loc['std',:].isnull()))].shape[1])
   
    avalia_1 = df.loc[:,(list(description.loc['std',:] == 0)) & (description.loc['count',:]==df.shape[0])].columns.values
    avalia_2 = df.loc[:,(list(description.loc['std',:] == 0)) & (description.loc['count',:]!=df.shape[0])].columns.values
    avalia_3 = df.loc[:,(list(description.loc['std',:].isnull())) & (description.loc['count',:]!=df.shape[0])].columns.values
   
    exclui_variaveis = {}
    exclui_variaveis['tipo_1'] = avalia_1
    exclui_variaveis['tipo_2'] = avalia_2
    exclui_variaveis['tipo_3'] = avalia_3
   
    return exclui_variaveis
 
 
def elimina_variaveis(df,parametros):
   
    print('eliminando variaveis dos tipos 1 e 2')
    
    df = df.loc[:,~df.columns.isin(list(parametros['tipo_1']))]
    df = df.loc[:,~df.columns.isin(list(parametros['tipo_2']))]
   
    return df
