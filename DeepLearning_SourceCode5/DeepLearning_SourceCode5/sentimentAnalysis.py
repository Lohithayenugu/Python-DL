#!pip install tensorboardcolab
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#from tensorboardcolab import *
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
import re
from keras.engine.saving import load_model
from sklearn.preprocessing import LabelEncoder
import numpy as np
from keras.callbacks import TensorBoard
data = pd.read_csv('Sentiment.csv')
#tbc = TensorBoardColab()
# Keeping only the neccessary columns
data = data[['text','sentiment']]

data['text'] = data['text'].apply(lambda x: x.lower())
data['text'] = data['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))

for idx, row in data.iterrows():
    row[0] = row[0].replace('rt', ' ')

max_fatures = 2000
tokenizer = Tokenizer(num_words=max_fatures, split=' ')
tokenizer.fit_on_texts(data['text'].values)
X = tokenizer.texts_to_sequences(data['text'].values)
max=0
for i in X:
  if len(i)>max:
    max=len(i)
#print(max)
#print(X)
#print("----------------------")
X = pad_sequences(X)

#print(len(X[0]))
embed_dim = 128
lstm_out = 196
def createmodel():
    model = Sequential()
    #print(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
    model.add(Embedding(max_fatures, embed_dim,input_length = X.shape[1]))
    model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(3,activation='softmax'))
    model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
    return model
# print(model.summary())

labelencoder = LabelEncoder()
integer_encoded = labelencoder.fit_transform(data['sentiment'])
y = to_categorical(integer_encoded)
X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size = 0.33, random_state = 42)

batch_size = 32
model = createmodel()
#model.fit(X_train, Y_train, epochs = 1, batch_size=batch_size, verbose = 2)

tensorboard = TensorBoard(log_dir="logs1/{}",histogram_freq=0, write_graph=True, write_images=True)
model.fit(X_train, Y_train, nb_epoch=1, batch_size=32,callbacks=[tensorboard])
score,acc = model.evaluate(X_test,Y_test,verbose=2,batch_size=batch_size)
print(score)
print(acc)
print(model.metrics_names)
model.save('my_model.h5')
model1 = load_model('my_model.h5')
from keras.preprocessing import text

text = np.array(['Didnt catch the full GOPdebate last night Here are some of Scotts best lines in 90 seconds Walker16'])
#print(text.shape)

pred=tokenizer.texts_to_sequences(text)
pred=pad_sequences(pred,maxlen=28)
#print(pred)
print("---------------------------------")
model1.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model1.predict(pred))
print(model1.predict_classes(pred))
#print(Y_test)
