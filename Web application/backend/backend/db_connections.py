import pymysql
import pandas

def mysql_to_csv() :
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='admin', password='koepPluoqHNjcbe8', database='pdg')
    query = 'select * from model_denguecase'

    results = pandas.read_sql_query(query, conn)
    results.to_csv("src/Data.csv", index=False)