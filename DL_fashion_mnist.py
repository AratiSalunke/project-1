import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

def main():
    print(" Version of installed Tensorflow is", tf.__version__)
    
    fashion_mnist = keras.datasets.fashion_mnist
    
    (train_images, train_labels),(test_images ,test_labels) = fashion_mnist.load_data()
    
    print("fashion_mnist dataset loaded successfully")
    
    class_name = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
    
    print("size of training dataset is",train_images.shape)
    
    print("label of training dataset are",train_labels)
    
    print("size of testing dataset ",test_images.shape)
    
    print("labels of testing dataset are",test_labels)
    
    for i in range(10):
       plt.figure()
       plt.imshow(train_images[i])
       plt.colorbar()
       plt.grid(False)
       plt.title("marvellous infosystems : image")
       plt.show()

       train_images = train_images / 255.0
       test_images = test_images / 255.0
 
       plt.figure(figsize = (10,10))
       for i in range(25):
           plt.subplot(5,5,i+1)
           plt.xticks([])
           plt.yticks([])
           plt.grid(False)
           plt.imshow(train_images[i],cmap = plt.cm.RdBu)
           plt.xlabel(class_name[train_labels[i]])
       plt.show()   
       
       model = keras.Sequential([keras.layers.Flatten(input_shape = (28,28)),keras.layers.Dense(128, activation = tf.nn.relu),keras.layers.Dense(10,activation = tf.nn.softmax)])
       
       model.compile(optimizer = 'adam',loss ='sparse_categorical_crossentropy',metrics = ['accuracy'])
       
       model.fit(train_images,train_labels,epochs = 10)
       
       test_loss,test_acc = model.evaluate(test_images,test_labels)
       
       print(test_acc)
 
       predictions = model.predict(test_images)

       print("Predicted values for first images =")
       print(predictions[0])

       print("--------------------------------------------------------------------------------------")
       print("Output of Image predictor after training ")
       print("--------------------------------------------------------------------------------------")
       for i in range(10):
            print("Expected Image :",class_name[test_labels[i]])
            print("Predicted Image :",class_name[np.argmax(predictions[i])])
            print("--------------------------------------------------------------------------------------")


if __name__ == "__main__":
     
     print("Marvellous Infosystem : Python Automation & Machine Learnig ")
     
     print("Fashion mnist data set ")
     print("Image classification application based on Deep learning ")
     main()




