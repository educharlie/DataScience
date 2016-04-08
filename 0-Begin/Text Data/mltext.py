from sklearn.datasets import fetch_20newsgroups

cats = ['alt.atheism', 'soc.religion.christian',  'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups( subset='train', categories=cats)
twenty_test = fetch_20newsgroups(subset='test', categories=cats)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer(use_idf=True)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

from sklearn.naive_bayes import MultinomialNB
nb_classifier = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

docs_test = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_test)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = nb_classifier.predict(X_new_tfidf)

for doc, category in zip(docs_test, predicted):
     print('{} => {}'.format(doc, twenty_train.target_names[category]))