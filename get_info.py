import praw, json
from pprint import pprint
from time import time


def get_info():
    reddit = praw.Reddit(client_id='kJnbFBn4D5XsWw',client_secret='zNFFGLE2t28P9s2eAY5-Cxu-OPQ', user_agent='web app:reddisFlair:v1.1 (by /u/00NoisyMime00)')

    data = []

    with open('id.json', 'r') as f:
        ids = json.load(f)

        
    for index, id in enumerate(ids):

        # gives the instance of that post
        submission = reddit.submission(id=id)

        # gives title of that post
        title = submission.title

        # gives all comments of that post
        submission.comments.replace_more(limit=None)
        comments = []
        for comment in submission.comments.list():
            comments.append(comment.body)
            

        # gives url
        url = 'www.reddit.com'+submission.permalink

        # gives the contents of the post
        content_of_post = submission.selftext
        
        # gives the timestamp
        timestamp = submission.created
        
        # gives the author
        author = str(submission.author)


        upvotes = submission.score
        

        upvote_ratio = submission.upvote_ratio

        flair_text = submission.link_flair_text
        

        data.append({'id':id, 'title':title, 'link':url, 'timestamp':timestamp, 'user-handle':author, 'flair':flair_text, 'upvotes':upvotes, 'upvotes_ratio':upvote_ratio, 'text_content':content_of_post, 'comments':comments})
        if index % 10 == 0:
            with open('full_data.json', 'w') as f:
                json.dump(data, f)


if __name__ == '__main__':
    get_info()