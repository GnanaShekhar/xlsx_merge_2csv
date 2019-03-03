import pandas as pd
import json
from datetime import datetime
from pprint import pprint
import copy
import os
from progress.bar import Bar

def main():
    #Get list of all the files
    file_list = os.listdir('xlsx/')0
    #Initialize output list
    outlist = []
    if len(file_list)>0:
        pprint(file_list)
        bar = Bar(message='processing',max=len(file_list))
        #For each file in file list read the rows using pandas
        #Convert the DataFrame to list and append to output list
        for file in file_list:
            bar.next()
            first = pd.ExcelFile('xlsx/'+file)
            df1 = first.parse('Sheet1')
            df1_list = df1.values.tolist()
            outlist.extend(df1_list)
        #Convert output list to DataFrame and define the column names
        df = pd.DataFrame(outlist, columns=['col1','col2','col3'])
        #Save the output in csv format
        df.to_csv('merged.csv', index=False)
    else:
        print('Input xlsx folder is empty!')

if __name__ == '__main__':
    main()
