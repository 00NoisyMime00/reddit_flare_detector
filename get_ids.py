import praw
import requests
import math, time
from datetime import datetime
import json
from pprint import pprint

def get_ids():
    # using the pushshift api needs a start time and end time for getting reddit posts
    end = math.floor(time.time())

    # this is the api, start represents the time after which you want the posts and before is the time before
    # which you want the posts to be
    # size represents the number of posts and can be 500 at max per call
    url = 'https://api.pushshift.io/reddit/search/submission?subreddit=india&after={}&before={}&size=500'

    count = 0

    id = []

    s = 0       #represents sports
    st = 0      #represents science and technology
    ai = 0      #represents ask india
    re = 0      #represents reddiquette
    b = 0       #represents business and finance

    # get a total of 10000 posts
    while count < 10000:
        
        # we take posts with a span of 5 hours
        start = end - 18000

        # pushshift.io api call made, returns a json object which contains an array of js objects under ['data]
        r = requests.get(url.format(start, end))
        posts = r.json()['data']
        
        for post in posts:
            try:
                # take only popular posts with the following flairs
                if post['score'] > 50 and (post['link_flair_text'] == 'Sports' or post['link_flair_text'] == 'Science/Technology' or post['link_flair_text'] == 'AskIndia'  or post['link_flair_text'] == '[R]eddiquette' or post['link_flair_text'] == 'Business/Finance'):
                    if post['link_flair_text'] == 'Sports':
                        s += 1
                    elif post['link_flair_text'] == 'Science/Technology':
                        st += 1
                    elif post['link_flair_text'] == 'AskIndia':
                        ai += 1
                    elif post['link_flair_text'] == 'Policy/Economy':
                        pe += 1
                    elif post['link_flair_text'] == '[R]eddiquette':
                        re += 1
                    elif post['link_flair_text'] == 'Business/Finance':
                        b += 1
                    # check if id already doesn't exist and if not, save it
                    try:
                        id.index(post['id'])
                    except:
                        id.append(post['id'])
            except:
                continue

        # represents the total number of posts saved so far 
        count = len(id)
        print(count, s, st, ai, re, b)

        # save the posts after every 10 new posts so in case of an error, we still have the data collected so far
        if count % 10:
            with open('id.json', 'w') as f:
                json.dump(id, f)

        # change end, so we can have posts from 5 hours before of the current time
        end = start

if __name__ == '__main__':
    get_ids()

