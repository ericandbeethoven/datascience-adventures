import sqlite3 as lite
import sys

con = None

try:
    # TABLE -> frequency(docid, term, count)
    con = lite.connect('reuters.db')
    # declare cursor
    cur = con.cursor()    

    # Q1
    sql =  """
    SELECT count(*) FROM (
    SELECT * FROM frequency WHERE docid = '10398_txt_earn'
    );  -- x is optional"""

    # Q2
    sql = """
    SELECT count(*) FROM (
    SELECT term FROM frequency 
    WHERE docid = '10398_txt_earn' 
    AND count = 1
    );  -- x is optional"""

    # Q3
    sql = """
    SELECT count(*) FROM (
    SELECT term FROM frequency 
    WHERE docid = '10398_txt_earn' 
    AND count =1 
    UNION
    SELECT term FROM frequency 
    WHERE docid = '925_txt_trade' 
    AND count = 1
    );  -- x is optional"""
    
    # Q4
    sql = """
    SELECT * FROM frequency
    WHERE term LIKE 'parliament'
    """

    res = cur.execute(sql).fetchall()
    print "{0}\n\nCount = {1}".format(res, len(res))
    
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
