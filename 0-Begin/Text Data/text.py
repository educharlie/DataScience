fsipa = open('sipatext.txt', 'r')
sipatext = fsipa.read()
fsipa.close()
#print(sipatext)

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()
word_counts = count_vect.fit_transform([sipatext])
count_vectn = CountVectorizer(ngram_range =(2, 2))

count_vect2 = CountVectorizer(stop_words='english')
word_counts2 = count_vect2.fit_transform([sipatext])

print('{}'.format(word_counts))
print('{}'.format(count_vect.vocabulary_))

print('{}'.format(count_vectn))
print('{}'.format(count_vect2.vocabulary_))
print('{}'.format(word_counts2))
