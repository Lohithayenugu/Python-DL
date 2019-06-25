from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

tfidf_Vect = TfidfVectorizer()
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
# print(tfidf_Vect.vocabulary_)
clf = MultinomialNB()
neigh = KNeighborsClassifier()
clf.fit(X_train_tfidf, twenty_train.target)
neigh.fit(X_train_tfidf,twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted_nb = clf.predict(X_test_tfidf)
predicted_kn = neigh.predict(X_test_tfidf)
score_nb = metrics.accuracy_score(twenty_test.target, predicted_nb)
print("NB Accuracy"," ",score_nb)
score_kn = metrics.accuracy_score(twenty_test.target, predicted_kn)
print("KN Accuracy"," ",score_kn)
