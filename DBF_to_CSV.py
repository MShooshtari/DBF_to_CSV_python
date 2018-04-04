from dbfread import DBF
import pandas as pd

dbfFileName = 'dbf_file_name'
dbf = DBF(dbfFileName+'.dbf')
df = pd.DataFrame(iter(dbf))
df.to_csv(dbfFileName+'.csv', index=False)