import json, string

with open('train.json', 'r') as f:
    full_data = json.load(f)

import re
import nltk
import numpy as np

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

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


def train():
    texts = [row[0] for row in full_data]
    flairs = [row[1] for row in full_data]

    texts = [' '.join(process_text(text)) for text in texts]
    print('text processing done!')


    # uncomment if you want to save the processed file 

    # save_cleaned_data = []
    # for i in range(len(texts)):
    #     save_cleaned_data.append([texts[i],flairs[i]])
    # with open('train.json', 'w') as f:
    #     json.dump(save_cleaned_data, f)
    # print('text saved!')


    

    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5,max_df=0.7, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')


    train_vectors = tfidf.fit_transform(texts).toarray()



    print('vectorisation done!!')

    from sklearn.model_selection import train_test_split
    vectors_train, vectors_test, topics_train, topics_test = train_test_split(train_vectors, flairs, random_state = 0)

    print('data has been split!')


    from sklearn.svm import LinearSVC
    classifier = LinearSVC()

    classifier.fit(vectors_train, topics_train)

    print('classifier trained!')

    # uncomment to Predict with the testing set
    # from sklearn.externals import joblib
    # classifier = joblib.load('model.pkl')

    topics_pred = classifier.predict(vectors_test)

    print(topics_pred)
    print('prediction done!')

    # ..and measure the accuracy of the results
    from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
    print(confusion_matrix(topics_test, topics_pred))
    print(classification_report(topics_test, topics_pred))
    print(accuracy_score(topics_test, topics_pred))

    from sklearn.externals import joblib
    # Output a pickle file for the model
    joblib.dump(classifier, 'model.pkl') 


if __name__ == '__main__':
    train()