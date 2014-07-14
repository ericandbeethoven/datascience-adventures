""" 
Menu-driven program to fetch tweets
based on option selected by the user.
Options:
1. Twitter Stream API
2. Twitter Search API

Usage:
$ python twitter_fetch.py

Sample output:
--------------
1: Twitter Stream API
2: Twitter Search API
Enter choice(1/2): 2
Enter search terms: Neymar
Enter result count: 1
......
......
{"statuses":[{"metadata":{"result_type":"recent",.........................
"id":485514266548531200,"id_str":"485514266548531200",....................
"text":"RT @8Fact_Footballl: Neymar: \"They took away my dream of playing 
a World Cup final, but the dream of becoming world champion didn't end.\"",
"source":"\u003ca href=\"http:\/\/tapbots.com\/tweetbot\" ...............
......
......
"""

import oauth2 as oauth
import urllib2 as urllib
import os
import sys
# See assignment1.html instructions or README for how to get these credentials

api_key = os.environ.get("TWITTER_KEY")
api_secret = os.environ.get("TWITTER_SECRET")
access_token_key = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_SECRET")

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response               

def fetchstream():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  # for line in response:
  #   print line.strip()
  if response:
    f = open('output.txt','wb')
    try:
      for line in response:
        print line.strip()
        f.write(line.strip())
        f.write('\n')
    except:
      f.close()
  else:
    quit("\nGot no response!")


def fetchsearched():
  url = "https://api.twitter.com/1.1/search/tweets.json"
  #terms = ' '.join(sys.argv[1:])
  terms = raw_input("Enter search terms: ")
  parameters = {
    'q': terms,
    'count': int(raw_input("Enter result count: "))
  } 
  response = twitterreq(url, "GET", parameters)
  # for line in response:
  #   print line.strip()
  if response:
    f = open('output.txt','wb')
    try:
      for line in response:
        print line.strip()
        f.write(line.strip())
        f.write('\n')
    except:
      f.close()
  else:
    quit("\nGot no response!")

      
if __name__ == '__main__':
  try:
    print "1: Twitter Stream API\n2: Twitter Search API"
    choice = int(raw_input("Enter choice(1/2): "))
  except:
    quit("\nWrong input!")
  if choice == 1:
    fetchstream()
  elif choice == 2:
    fetchsearched()
  else:
    quit("\nWrong choice!")

