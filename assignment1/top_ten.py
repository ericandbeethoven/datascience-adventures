# http://econym.org.uk/gmap/states.xml <- polygon based coordinates of the US states.

import sys
import json
from operator import itemgetter
from collections import Counter

def flatten(L):
  if L==[]:
    return []
  elif isinstance(L[0],list):
     return flatten(L[0])+flatten(L[1:])
  else:
     return L[:1]+flatten(L[1:])
            
def main():
    """
    Return the state code of the happiest US state
    """
    with open(sys.argv[1]) as f:
        entities = filter(None, 
                          [json.loads(line).get('entities',None) 
                           for line in f])
    tags = flatten(filter(list, [x['hashtags'] for x in entities]))
    new = Counter([x['text'] for x in tags])
    top = sorted(new.iteritems(), key=itemgetter(1))
    for i in top[-10:][::-1]: sys.stdout.writelines('{0} {1}\n'.format(i[0].encode('utf-8'), i[1]))

if __name__ == '__main__':
    main()
