from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import Callback
from sklearn.metrics import confusion_matrix
import random
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt


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
        self.model.add(Dense(128, input_dim=input_size, activation='relu'))
        self.model.add(Dropout(0.3)) 
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dropout(0.3))
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dense(output_size, activation='softmax'))

    def compile(self):
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


class MetricsCallback(Callback):

    def __init__(self, X_val, y_val):
        super().__init__()
        self.X_val = X_val
        self.y_val = y_val
        self.metrics = {'loss': [], 'accuracy': [], 'val_loss': [], 'val_accuracy': []}

    def on_train_begin(self, logs={}):
        self.metrics = {'loss': [], 'accuracy': [], 'val_loss': [], 'val_accuracy': []}

    def on_epoch_end(self, epoch, logs={}):
        self.metrics['loss'].append(logs.get('loss'))
        self.metrics['accuracy'].append(logs.get('accuracy'))
        self.metrics['val_loss'].append(logs.get('val_loss'))
        self.metrics['val_accuracy'].append(logs.get('val_accuracy'))

    def on_train_end(self, logs={}):
        self.visualize()
        self.plot_confusion_matrix()

    def plot_confusion_matrix(self):
        # Realizar predicciones en el conjunto de validación
        predictions = self.model.predict(self.X_val)
        predictions = np.argmax(predictions, axis=1)
        y_true = np.argmax(self.y_val, axis=1)

        # Calcular la matriz de confusión
        cm = confusion_matrix(y_true, predictions)
        sns.heatmap(cm, annot=True, fmt="d")
        plt.title('Matriz de Confusión')
        plt.ylabel('Etiquetas Reales')
        plt.xlabel('Etiquetas Predichas')
        plt.show()

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

    def on_train_end(self, logs={}):
        self.visualize()
        self.plot_confusion_matrix()
