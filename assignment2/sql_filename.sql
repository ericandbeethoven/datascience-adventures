-- TABLE -> frequency(docid, term, count)
-----------------------------------------
-- docid is a document identifier corresponding to a particular file of text	
-- term is an English word, 
-- and count is the number of the occurrences of the term within the document indicated by docid.

SELECT * FROM frequency WHERE docid = '991_txt_trade';
SELECT count(*) FROM frequency;
