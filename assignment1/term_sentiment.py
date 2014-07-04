import sys
import json
import string
import unicodedata

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

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
    c = 0
    unlisted_scores = {}
    #wordlist = set(open('/usr/share/dict/words','r').read().split('\n'))
    for line in tweet_file:
        c+=1
        temp = json.loads(line.strip())
        try:
            sentence = unicodedata.normalize('NFKD', temp['text']).encode('ascii','ignore')
            words = ' '.join(sentence.translate(table, string.punctuation).translate(table, '0123456789').split()).split()
            #filtered = list(set([x.lower() for x in words if len(x) >= 3]) - set(scores.keys()) & wordlist)
            filtered_listed = list(set([x.lower() for x in words]) & set(scores.keys()))
            filtered_unlisted = list(set([x.lower() for x in words if len(x) >= 3]) - set(scores.keys()) - set(stopwords))
            sentiment = sum([scores[x] for x in filtered_listed])
            if filtered_unlisted:
                    for x in filtered_unlisted:
                        try:
                            unlisted_scores[x] += float(sentiment)/len(filtered_listed)
                            unlisted_scores[x] /= 2
                        except:
                            unlisted_scores[x] = float(sentiment)/len(filtered_listed)
            # if sentiment:
            #     print sentiment, filtered
            # else:
            #     print sentiment
            # print c, ' - sentiment -', sentiment
            # print c, ' - listed ---- ', filtered_listed
            #print c, ' - unlisted -- ', filtered_unlisted
        except:
            continue
            #raise
    for i,x in unlisted_scores.iteritems(): print i,x

if __name__ == '__main__':
    main()
