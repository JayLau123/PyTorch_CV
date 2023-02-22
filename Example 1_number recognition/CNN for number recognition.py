#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# import data set with handwritten digits 0-9
# 60,000 for training; 10,000 for validation
# Note: If "mnist.npz" is in ~/.keras/datasets, it will not have to download

from keras.datasets import mnist

#download mnist data and split into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# In[2]:


print ('Size of training data set: ',len(X_train))
print ('Size of validation data set: ',len(X_test))


# In[3]:


# original data is 60000 images of 28x28 pixels
# The original test outcomes are useful later, so I save them prior to
# hot-one encoding
y_test_original = y_test

#plot arbitrary image in the dataset


for i in range(10):
    plt.imshow(X_train[i])
    plt.show()
    print('The answer for this image is: ', y_train[i])

print ('Pixel dimension of individual image: ',X_train[0].shape) #check image shape


# In[4]:


# reshape data to fit model:
# in greyscale format (signified by last argument "1")

X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)

# the output values need to be mapped onto a "hot-one" array
# since there are 10 possible output values, this array will have length 10 (0,1,2,3...9)

from keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# confirm for our example digit
#print(y_train[135])

# build the model
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, Dropout, BatchNormalization


# In[5]:


a=0.4 # dropout rate

model = Sequential() # create model

model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1))) # add model layers, with 3x3 filter and ReLU activation

model.add(Dropout(a)) # each layer has a drapout rate, same or different
model.add(BatchNormalization()) # normalize



# 2nd layer
model.add(Conv2D(32, kernel_size=3, activation='relu'))
# Dropout
model.add(Dropout(a))
# normalize
model.add(BatchNormalization())



model.add(Flatten()) # prepare output of 32x32 layer for dense layer, by flattening it

model.add(Dense(10, activation='softmax')) # lastly, the output layer, with SoftMax activation

model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy']) #compile model using accuracy to measure model performance

print(model.summary())

# train the model
#
# in a single epoch, the entire training set is passed through the network
# once (forward and backward), and the weights are updated
# 
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)
model.save('numbers_trained')


# In[ ]:




