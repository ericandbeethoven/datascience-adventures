"""
Produces sentiments per tweet.

Usage:
$ python tweet_sentiment.py AFINN-111.txt  output2.txt  

Sample output:
    -3
    0
    0
    -1
    0
    6
    0
    3
"""

import sys
import json
import string
import unicodedata

def main():
    """ 
    read AFINN classified mood file and tweet dumps,
    classify tweet sentiments and produce new output.
    """
    afinnfile = open(sys.argv[1]) #AFINN first
    tweet_file = open(sys.argv[2]) #tweet dump second arg

    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    table = string.maketrans("","") # step 1 of removing punctuations      
    final = []
    for line in tweet_file:
        temp = json.loads(line.strip())
        try:
            sentence = unicodedata.normalize('NFKD', temp['text']).encode('ascii','ignore')
            words = ' '.join(sentence.translate(table, string.punctuation).split()).split()
            filtered = list(set(scores.keys()) & set([x.lower() for x in words]))
            sentiment = sum([scores[x] for x in filtered])
            # if sentiment:
            #     print sentiment, filtered
            # else:
            #     print sentiment
            print sentiment
        except:
            print 0
            #continue
            #raise
if __name__ == '__main__':
    main()
