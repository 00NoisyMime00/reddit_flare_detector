# reddit_flare_detector.

The project predicts the flairs of posts on india subreddit.
link: https://flairinator-api-heroku.herokuapp.com/predict

## Motivation
Becoming a part of precog research group!!

## Tech/framework used
Ex.

<b>Built with</b>
- [Python](https://electron.atom.io)
- [Praw]()
- [pushshift api]()
- [Javascript]()

## Features
Dyanamic webpage! works with Ajax thus don't have to reload the page :D


## Installation
do pip install -r requirements.txt

## Tests
just get any link of a post from https://www.reddit.com/r/india
with flair among Science/Technology, Business/finance, political, non-political, [R]eddiquette, AskIndia 
paste the url in predict tab and press enter, and wait for the magic :D

## How to use?
just clone the repo.
Set up a python 3 virtual environment.
download the requirements by pip3 install -r requirements.txt
open you terminal and run main.py
it gets a set of 10000 new posts from reddit, and gets all the information about the posts then cleans the data, the final cleaned data is stored in the file train.json
then it starts training on that data and saves the trained model as model.pkl



## Credits
Give proper credits. This could be a link to any repo which inspired you to build this project, any blogposts or links to people who contrbuted in this project. 


## License
A short snippet describing the license (MIT, Apache etc)

MIT © [Nikunj Singhal]()
