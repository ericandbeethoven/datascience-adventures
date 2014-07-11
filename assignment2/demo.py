import sqlite3 as lite
import sys

con = None

try:
    # TABLE -> frequency(docid, term, count)
    con = lite.connect('reuters.db')
    # frequency = {'docid' : [],
    #              'term' : [],
    #              'count' : []}

    # declare cursor
    cur = con.cursor()    
    # test command
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data                
    
    # entry count
    cur.execute('SELECT count(*) FROM frequency')
    print "Entry count: %s" % cur.fetchone()

    # sample data
    cur.execute("SELECT * FROM frequency WHERE docid = '991_txt_trade'")
    freq = dict(zip(['docid', 'term', 'count'], cur.fetchone())) #fetchall
    print "Sample data: \n", freq

    ## sample commands
    # # Create table as per requirement
    # sql = """CREATE TABLE demo (
    #          FIRST_NAME  CHAR(20) NOT NULL,
    #          LAST_NAME  CHAR(20),
    #          AGE INT,  
    #          SEX CHAR(1),
    #          INCOME FLOAT )"""
    # cur.execute(sql)
    
except lite.Error, e:    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:    
    if con:
        con.close()


