"""
Usage:
$ python top_ten.py output.txt

Sample Output:
--------------
  CallMeCam 18
  EnLaHighSiempreEsta 18
  gameinsight 17
  bringbackthereal1dfandom 14
"""

import sys
import json
from operator import itemgetter
from collections import Counter


def flatten(L):
    """
    Flattens lists.
    Example: [[1,2],[3,4],5] --> [1,2,3,4,5]
    """
    if L == []:
        return []
    elif isinstance(L[0], list):
        return flatten(L[0]) + flatten(L[1:])
    else:
        return L[:1] + flatten(L[1:])


def main():
    """
    Return top ten frequently used hashtags.
    """
    with open(sys.argv[1]) as f:
        # extract 'entities' field from the tweet object
        entities = filter(None,
                          [json.loads(line).get('entities', None)
                           for line in f])
    # extract hashtag objects and flatten the list
    tags = flatten(filter(list, [x['hashtags'] for x in entities]))
    # Count the frequencies of the hashtags
    new = Counter([x['text'] for x in tags])
    # sort accordingly
    top = sorted(new.iteritems(), key=itemgetter(1))
    # print top 10 hashtags
    for i in top[-10:][::-1]:   
        sys.stdout.writelines('{0} {1}\n'.format(i[0].encode('utf-8'), i[1]))

if __name__ == '__main__':
    main()
