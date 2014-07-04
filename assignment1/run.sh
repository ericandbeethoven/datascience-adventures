#!/bin/sh
echo "--------------------------------"
echo "Results of tweet_sentiment.py .. \n"
python tweet_sentiment.py AFINN-111.txt  output.txt
echo "--------------------------------"
echo "Results of term_sentiment.py .. \n"
python term_sentiment.py AFINN-111.txt  output.txt
echo "--------------------------------"
