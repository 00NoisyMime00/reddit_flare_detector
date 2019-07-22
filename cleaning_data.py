'''

    Does manual cleaning of the data, eg. removes all links, and removes comments
    which are deleted. and comments by robot(which start with ^).

    It uses the post_info file. where the cleaning is done. Had to use two different files because this
    is used for training the data on machine while that is used on the flask app.

'''

import json
from post_info import post_contents

def cleaning_data():
    st = 0
    r = 0
    ai = 0
    p = 0
    b = 0
    np = 0
    pe = 0
    s = 0

    with open('train.json', 'r') as f:
        posts = json.load(f)

    filtered_posts = list(posts)


    for index in posts:
        
        post = index
        
        if post['flair'] == 'Science/Technology':
            st += 1
        elif post['flair'] == 'AskIndia':
            ai += 1
        elif post['flair'] == 'Politics':
            p += 1
        elif post['flair'] == 'Business/Finance':
            b += 1
        elif post['flair'] == 'Non-Political':
            np += 1
        elif post['flair'] == 'Sports':
            s += 1
        elif post['flair'] == '[R]eddiquette':
            r += 1
        else:
            filtered_posts.remove(index)
            
    print('Science/Technology', st)
    print('AskIndia', ai)
    print('Politics', p)
    print('Business/Finance', b)
    print('Non-Political', np)
    print('Sports', s)
    print('[R]eddiquette', r)

    posts = list(filtered_posts)
    data = []

    for index in posts:
        post = index
        contents = post_contents(post, False)
        data.append([contents, post['flair']])

    with open('train.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    cleaning_data()