import pandas as Pa
Pa.options.mode.chained_assignment = None

da = Pa.read_csv('/Users/yashmalik/Desktop/cs_prinAP.csv')

heads = list(da.columns)
countStudent = len(da.index)
for head in heads:
    firstIt = da[head][0]
    if not Pa.isna(firstIt) and not type(firstIt) == str and not firstIt == 0.0:   
        factor = 100/firstIt
        for i in range(countStudent):
            da[head][i] *= factor
da.to_csv('normalizedGradesPrinAP.csv')
        
