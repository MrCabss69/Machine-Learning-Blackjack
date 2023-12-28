from keras.models import Sequential
from keras.layers import Conv2D, Flatten, Dense, Dropout
import random

class DummyNetwork:
    def get_action(self, estado):
        actions = estado.get_available_actions()
        return random.choice(actions)



class BlackjackNN:
    def __init__(self, input_size, output_size):
        self.model = Sequential()
        self.model.add(Dense(128, input_dim=input_size, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(output_size, activation='softmax'))

    def compile(self):
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        
        

class BlackjackCNN:
    def __init__(self, input_shape, output_size):
        self.model = Sequential()
        self.model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))
        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(Flatten())
        self.model.add(Dense(128, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(output_size, activation='softmax'))

    def compile(self):
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

