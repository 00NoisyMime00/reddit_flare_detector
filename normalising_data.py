'''

    This file is used to normalise the data, the data collected was uneven with some
    flairs being really high in number, thus we normalise the posts.

'''

import json, random




def normalising_data():

    with open('full_data.json', 'r') as f:
        posts = json.load(f)
        
    st = []
    ai = []
    p = []
    bf = []
    np = []
    s = []
    r = []

    for post in posts:

        if post['flair'] == 'Science/Technology':
            st.append(post)
        elif post['flair'] == 'AskIndia':
            ai.append(post)
        elif post['flair'] == 'Politics':
            p.append(post)
        elif post['flair'] == 'Business/Finance':
            bf.append(post)
        elif post['flair'] == 'Non-Political':
            np.append(post)
        elif post['flair'] == 'Sports':
            s.append(post)
        elif post['flair'] == '[R]eddiquette':
            r.append(post)

    posts = []


    for i in [st, ai,p,bf,np,s,r]:
        # sorts the posts in a particular flair type in reverse order of number of upvotes and take top 500
        i = sorted(i, key = lambda j: j['upvotes'], reverse=True)

        if len(i) > 500:
            i = i[:500]

        posts += i
        
    

    with open('train.json','w') as f:
        json.dump(posts,f)    


if __name__ == '__main__':
    normalising_data()