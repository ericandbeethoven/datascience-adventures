-- TABLE -> frequency(docid, term, count)
-----------------------------------------
-- docid is a document identifier corresponding to a particular file of text	
-- term is an English word, 
-- and count is the number of the occurrences of the term within the document indicated by docid.

-- Test query: SELECT * FROM frequency WHERE docid = '991_txt_trade';

SELECT count(*) FROM (
       -- Q1
       -- SELECT * FROM frequency WHERE docid = '10398_txt_earn' 
       
       -- Q2
       -- SELECT term FROM frequency 
       -- WHERE docid = '10398_txt_earn' 
       -- AND count = 1

       -- Q3
       -- SELECT term FROM frequency 
       -- WHERE docid = '10398_txt_earn' 
       -- AND count =1 
       -- UNION
       -- SELECT term FROM frequency 
       -- WHERE docid = '925_txt_trade' 
       -- AND count = 1
       
       -- Q4
       SELECT * FROM frequency 
       WHERE term LIKE 'parliament'
       
) x;  -- x is optional
