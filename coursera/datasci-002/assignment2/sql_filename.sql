-- TABLE -> frequency(docid, term, count)
-----------------------------------------
-- docid is a document identifier corresponding to a particular file of text	
-- term is an English word, 
-- and count is the number of the occurrences of the term within the document indicated by docid.

-- Test query: SELECT * FROM frequency WHERE docid = '991_txt_trade';

SELECT count(*) FROM (
       -- 1.a
       -- SELECT * FROM frequency WHERE docid = '10398_txt_earn' 
       
       -- 1.b
       -- SELECT term FROM frequency 
       -- WHERE docid = '10398_txt_earn' 
       -- AND count = 1

       -- 1.c
       -- SELECT term FROM frequency 
       -- WHERE docid = '10398_txt_earn' 
       -- AND count =1 
       -- UNION
       -- SELECT term FROM frequency 
       -- WHERE docid = '925_txt_trade' 
       -- AND count = 1
       
       -- 1.d
       -- SELECT * FROM frequency 
       -- WHERE term LIKE 'parliament'
       
       -- 1.e
       -- SELECT DISTINCT docid FROM frequency
       -- GROUP BY docid
       -- HAVING SUM(count) > 300
             
       -- 1.f
       SELECT DISTINCT docid FROM frequency              
       WHERE term LIKE 'transactions'
       OR term LIKE 'world'

) x;  -- x is optional

