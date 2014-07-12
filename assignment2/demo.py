import sqlite3 as lite
import sys

con = None

try:
    # TABLE -> frequency(docid, term, count)
    con = lite.connect('reuters.db')
    # declare cursor
    cur = con.cursor()    

    # # 1.a
    # sql =  """
    # -- SELECT count(*) FROM (
    # SELECT * FROM frequency WHERE docid = '10398_txt_earn'
    # -- );  -- x is optional
    # """

    # # 1.b
    # sql = """
    # SELECT term FROM frequency 
    # WHERE docid = '10398_txt_earn' 
    # AND count = 1
    # """

    # # 1.c
    # sql = """
    # SELECT term FROM frequency 
    # WHERE docid = '10398_txt_earn' 
    # AND count =1 
    # UNION
    # SELECT term FROM frequency 
    # WHERE docid = '925_txt_trade' 
    # AND count = 1
    # """
    
    # # 1.d
    # sql = """
    # SELECT * FROM frequency
    # WHERE term LIKE 'parliament'
    # """

    # # 1.e
    # #sql = "SELECT SUM(count) FROM frequency WHERE docid = '8441_txt_acq';"
    # sql = """
    # SELECT DISTINCT docid FROM frequency
    # GROUP BY docid
    # HAVING SUM(count) > 300"""
    
    # 1.f
    sql = """
    SELECT docid FROM frequency
    GROUP BY docid
    HAVING term LIKE 'transactions' OR term LIKE 'world'
    """ 
    # sql = "SELECT term FROM frequency WHERE docid = '9712_txt_trade';"
    
    res = cur.execute(sql).fetchall()
    print "{0}\n\nCount = {1}".format(res, len(res))
    # FIX: print bool('9795_txt_trade' in [i[0] for i in res]) == False

    # frequency = {'docid' : [],
    #              'term' : [],
    #              'count' : []}
    # test command
    # cur.execute('SELECT SQLITE_VERSION()')
    # data = cur.fetchone()
    # print "SQLite version: %s" % data                
    
    # # entry count
    # cur.execute('SELECT count(*) FROM frequency')
    # print "Entry count: %s" % cur.fetchone()

    # # sample data
    # cur.execute("SELECT * FROM frequency WHERE docid = '991_txt_trade'")
    # freq = dict(zip(['docid', 'term', 'count'], cur.fetchone())) #fetchall
    # print "Sample data: \n", freq

except lite.Error, e:    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:    
    if con:
        con.close()
