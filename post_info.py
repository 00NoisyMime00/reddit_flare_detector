import praw

reddit = praw.Reddit(client_id='kJnbFBn4D5XsWw',client_secret='zNFFGLE2t28P9s2eAY5-Cxu-OPQ', user_agent='web app:reddisFlair:v1.1 (by /u/00NoisyMime00)')
subreddit = reddit.subreddit('india')

def post_contents(url, is_url = True):

    info = ''

    if is_url == True:
        submission = reddit.submission(url=url)

        title = submission.title
        text_content = submission.selftext
        submission.comments.replace_more(limit=None)
        comments = []
        for comment in submission.comments.list():
            comment = comment.body
            comment = comment.split('\n')
            comment = ' '.join(comment)
            if (comment != '[deleted]' or comment != '[removed]') and comment != '' and '^' not in comment:
                count = 0
                
                while 'http' in comment:
                    count += 1
                    http_pos = comment.find('http')
                    
                    if comment.find(' ', http_pos):
                        comment = comment[:http_pos] + comment[comment.find(' ', http_pos):]

                    if count >= 50:
                        break
                    if 'http' not in comment:
                        break
                comments.append(comment)

        comments = ' '.join(comments)
        
    else:
        title = url['title']
        text_content = url['text_content']

        comments = []
        for comment in url['comments']:
            comment = comment.split('\n')
            comment = ' '.join(comment)
            if (comment != '[deleted]' or comment != '[removed]') and comment != '' and '^' not in comment:
                count = 0
                
                while 'http' in comment:
                    count += 1
                    http_pos = comment.find('http')
                    
                    if comment.find(' ', http_pos):
                        comment = comment[:http_pos] + comment[comment.find(' ', http_pos):]

                    if count >= 50:
                        break
                    if 'http' not in comment:
                        break
                comments.append(comment)

        comments = ' '.join(comments)
        
    if title != '' and title != '[deleted]' and title != '[removed]':
        count = 0   
        while 'http' in title:
            count += 1
            http_pos = title.find('http')
            
            if title.find(' ', http_pos):
                title = title[:http_pos] + title[title.find(' ', http_pos):]
            if count >= 50:
                break
            if 'http' not in title:
                break
    else:
        title = ''
    
    if text_content != '' and text_content != '[deleted]' and text_content != '[removed]':
        count = 0   
        while 'http' in text_content:
            count += 1
            http_pos = text_content.find('http')
            
            if text_content.find(' ', http_pos):
                text_content = text_content[:http_pos] + text_content[text_content.find(' ', http_pos):]
            if count >= 50:
                break
            if 'http' not in text_content:
                break
    else:
        text_content = ''
    
    info = title + " " + text_content + " " + comments
    return info
    
    

# main('https://www.reddit.com/r/india/comments/cfus1u/are_there_any_support_groups_or_online_forums/')
# print(post_contents('https://www.reddit.com/r/india/comments/cfvy8p/man_running_away_from_dog_mistaken_as_thief_in_up/'))