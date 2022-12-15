import pandas as pd
from sqlalchemy import create_engine

import pymysql

from urllib.parse import quote

df = pd.read_csv("./data/national_universities_rankings_2021.csv")

df_to_sql = df.drop(columns=['Description'])

df_to_sql['Tuition and fees'] = df_to_sql['Tuition and fees'].map(lambda x: x.lstrip('$'))
df_to_sql['In-state'] = df_to_sql['In-state'].map(lambda x: x if pd.isnull(x) else x.lstrip('$'))

df_to_sql[['City', 'State']] = df_to_sql.Location.str.split(',',expand=True)
df_to_sql = df_to_sql.drop(columns=['Location'])

df_to_sql['source'] = './data/national_universities_rankings_2021.csv'

print(df_to_sql.head())

sqlEngine = create_engine('mysql+pymysql://root:%s@127.0.0.1/university' % quote('Root123'))

dbConnection = sqlEngine.connect()

df_to_sql.to_sql('university_rank', con=sqlEngine, if_exists='append')