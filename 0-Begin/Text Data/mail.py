docs_test = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_test)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = nb_classifier.predict(X_new_tfidf)

for doc, category in zip(docs_test, predicted):
     print('{} => {}'.format(doc, twenty_train.target_names[category]))

