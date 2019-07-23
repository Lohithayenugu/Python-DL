from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer, one_hot
import pandas as pd
from keras_preprocessing.sequence import pad_sequences
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
import numpy as np


df = pd.read_csv('SPAM_text.csv',encoding='latin-1')
sentences = df['Message'].values
y = df['Category'].values

max_review_len= max([len(s.split()) for s in sentences])
#tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(sentences)
#getting the vocabulary of data
sentences = tokenizer.texts_to_sequences(sentences)
padded_docs= pad_sequences(sentences,maxlen=max_review_len)

le = preprocessing.LabelEncoder()
y = le.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(padded_docs, y, test_size=0.25, random_state=1000)
vocab_size= len(tokenizer.word_index)+1
num_classes = y_test.shape[0]

model = Sequential()
model.add(layers.Embedding(vocab_size, 50, input_length=max_review_len))
#model.add(layers.Flatten())
model.add(Conv1D(32, 3, activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv1D(64, 3, activation='relu', padding='same'))
model.add(MaxPooling1D(pool_size=1))

model.add(Conv1D(128, 3, activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(Conv1D(128, 3, activation='relu', padding='same'))
model.add(MaxPooling1D(pool_size=1))


# flattening the matrix into vector form
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['acc'])

model.fit(X_train,y_train, epochs=5, verbose=True, validation_data=(X_test,y_test), batch_size=64)

# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
print("loss: %.2f%%" % (scores[0]*100))
model.save('./model' + '.h5')
