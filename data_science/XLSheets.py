'''
Module currently under development ...
'''

def XLSheetNames(path,):
    '''
    Returns all sheet names for any Excel spreadsheet
    '''
    import xlrd
    xls = xlrd.open_workbook(path, on_demand=True)
    sheet_names = xls.sheet_names()
    print('Sheet names:','\n',xls.sheet_names())
    return(sheet_names)

def XLSheetsToDictionary(path,sheet_names,ColNameIndex=1,skiprows=[0]):
    '''
    Converts Excel file into dictionary format
    '''
    d = {}
    for i in sheet_names:
        df_tmp = pd.read_excel(str(path),skiprows=skiprows,sheet_name=str(i))
        d[str(i)] = [df_tmp, df_tmp.iloc[:,ColNameIndex]]
    return(d)        

def ConvertLinesToColor(path,sheet_names,XLDictionary,):
    '''
    Adds new element key to XLDictionary with color information
    '''
    import openpyxl as px
    
    wb = px.load_workbook(path)
    
    for sheet_name in sheet_names: 
        sheet = wb.get_sheet_by_name(str(sheet_name))
        df_ = XLDictionary[str(sheet_name)][0]
        
        colors = []
        lines_per_sheet = df_.shape[0]
        
        ExcelIndex = ['A' + str(line) for (line) in range(3,lines_per_sheet)]
        
        for i in ExcelIndex:
            colors.append(sheet[str(i)].fill.start_color.index)
        
        colors = list(map(lambda x: str(x), colors))
        
        XLDictionary[str(sheet_name)].append(colors)  
        
    return (XLDictionary)
    
def AddColorLine(XLDictionary,):
    '''
    Adds new column to dataframe within dictionary with color line information
    '''
    for i in list(XLDictionary.keys()):
        df_ = XLDictionary[i][0] #access dataframe within dictionary, 0 position
        color_ = pd.DataFrame(XLDictionary[i][2]) #access color information within dictionary index >> 3rd position
        XLDictionary[i][0] = pd.concat([df_,color_],axis=1).rename({0:'LineColor'},axis=1)
    return(XLDictionary)

def AllColumns(XLDictionary,):
    '''
    List of all columns of all XL spreadsheets
    '''
    all_columns = []

    for i in list(XLDictionary.keys()):
        df_ = XLDictionary[i][0]
        col_names = list(df_.columns.values)
        all_columns.append(col_names)
    all_columns = list(set([item for sublist in all_columns for item in sublist]))
    
    return (all_columns)

def CodeToColor(XLDictionary, ColorDictionary):
    for i in list(XLDictionary.keys()):
        try:
            print(i,': Code information fulfilled')
            XLDictionary[i][0].LineColor = XLDictionary[i][0].LineColor.apply(lambda x: ColorDictionary[str(x)])
        except KeyError:
            print(i,': Code information missing')
            XLDictionary[i][0].LineColor = XLDictionary[i][0].LineColor.apply(lambda x: str(x))
    return(XLDictionary)

def CompareLists(l1,l2):

    match    = [i for i in l1 if i in l2]
    mismatch = [i for i in l1 if i not in l2]
        
    return match, mismatch

def PrintSideBySide(l1,l2): 
    import itertools
    
    match, mismatch = CompareLists(l1,l2)
    
    return [tuple(filter(lambda x: x is not None, i)) for i in itertools.zip_longest(match,mismatch)]