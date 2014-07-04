import sys
import json
from collections import Counter

def main():
    """ 
    Calculate Term Frequency for each term in all tweets
    """
    with open(sys.argv[1]) as tweet_file:
        _all = (json.loads(line).get('text', '').split() for line in tweet_file)
        frequencies = Counter(word for tweet in _all for word in tweet)

    total = sum(frequencies.values())
    for i,x in frequencies.iteritems(): print i,float(x)/total
    
if __name__ == '__main__':
    main()
