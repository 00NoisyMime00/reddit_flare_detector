from post_info import post_contents

from flask import Flask, render_template,url_for,request
import json, nltk, re, string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def process_text(text):
    # Make all the strings lowercase and remove non alphabetic characters
    text = re.sub('[^A-Za-z]', ' ', text.lower())

    # remove all numbers from the text
    text = re.sub(r'\d+', '', text).strip()

    # remove punctuation marks
    text = text.translate(str.maketrans('','',string.punctuation)).strip()

    # Substituting multiple spaces with single space
    text= re.sub(r'\s+', ' ', text, flags=re.I)
    

    # Tokenize the text; this is, separate every sentence into a list of words
    # Since the text is already split into sentences you don't have to call sent_tokenize
    tokenized_text = word_tokenize(text)

    # Remove the stopwords and stem each word to its root
    clean_text = [
        lemmatizer.lemmatize(word) for word in tokenized_text
        if word not in stopwords.words('english')
    ]

    # Remember, this final output is a list of words
    return clean_text


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')

    elif request.method == 'POST':

        url = request.form['url']
        contents = post_contents(url)
        contents = ' '.join(process_text(contents))

        with open('train.json', 'r') as f:
            full_data = json.load(f)
        
        texts = [row[0] for row in full_data]

        from sklearn.feature_extraction.text import TfidfVectorizer
        tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5,max_df=0.7, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')

        train_vectors = tfidf.fit_transform(texts).toarray()
        test_vectors = tfidf.transform([contents]).toarray()

        from sklearn.externals import joblib
        classifier = joblib.load('model.pkl')

        prediction = classifier.predict(test_vectors)
        print(prediction)
        j = str(prediction[0])
        return j

if __name__ == '__main__':
    app.run()