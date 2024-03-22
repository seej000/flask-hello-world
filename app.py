import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from --Seiji Aoyama-- in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_db_ofde_user:vW4uKLc4YKccVCmclWRbrSMDic72bkZt@dpg-cnul33fjbltc73c4fpmg-a/lab10_db_ofde")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://lab10_db_ofde_user:vW4uKLc4YKccVCmclWRbrSMDic72bkZt@dpg-cnul33fjbltc73c4fpmg-a/lab10_db_ofde")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return "Baseball Table Successfully Created"