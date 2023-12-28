from keras.models import Sequential
from keras.layers import Conv2D, Flatten, Dense, Dropout
import random
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import Callback

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
        

class BlackjackDNN:
    def __init__(self, input_size, output_size):
        self.model = Sequential()
        # Primera capa oculta
        self.model.add(Dense(128, input_dim=input_size, activation='relu'))
        self.model.add(Dropout(0.3))  # Agregar dropout para regularización

        # Segunda capa oculta
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dropout(0.3))  # Agregar dropout para regularización

        # Tercera capa oculta
        self.model.add(Dense(32, activation='relu'))

        # Capa de salida
        self.model.add(Dense(output_size, activation='softmax'))

    def compile(self):
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])




class MetricsCallback(Callback):
    def on_train_begin(self, logs={}):
        self.metrics = {'loss': [], 'accuracy': [], 'val_loss': [], 'val_accuracy': []}

    def on_epoch_end(self, epoch, logs={}):
        self.metrics['loss'].append(logs.get('loss'))
        self.metrics['accuracy'].append(logs.get('accuracy'))
        self.metrics['val_loss'].append(logs.get('val_loss'))
        self.metrics['val_accuracy'].append(logs.get('val_accuracy'))
    
    def visualize(self):
        # Visualizar las métricas
        plt.figure(figsize=(12, 5))

        # Pérdida
        plt.subplot(1, 2, 1)
        plt.plot(self.metrics['loss'], label='Entrenamiento')
        plt.plot(self.metrics['val_loss'], label='Validación')
        plt.title('Pérdida durante el Entrenamiento')
        plt.xlabel('Épocas')
        plt.ylabel('Pérdida')
        plt.legend()

        # Precisión
        plt.subplot(1, 2, 2)
        plt.plot(self.metrics['accuracy'], label='Entrenamiento')
        plt.plot(self.metrics['val_accuracy'], label='Validación')
        plt.title('Precisión durante el Entrenamiento')
        plt.xlabel('Épocas')
        plt.ylabel('Precisión')
        plt.legend()
        plt.show()