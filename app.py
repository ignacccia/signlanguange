from flask import Flask, render_template, request
import keras
from keras.preprocessing import image
import numpy as np
import os
from matplotlib import pyplot as plt

import keras.utils as image
import shutil

app = Flask(__name__, template_folder='template')

ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT    

def classification(fn):
        model_path = os.getcwd() + '/model.hdf5'
        model = keras.models.load_model(model_path)

        img = image.load_img(fn, target_size= (128,128))
        imgplot = plt.imshow(img)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis =0)

        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)
        print(classes)
        class_list = os.listdir("/content/Indian")

        for j in range(len(class_list)):
            if classes[0][j] == 1. :
                return class_list[j]

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['GET','POST'])
def predict():
    content_path = os.getcwd() + '/content/'
    static_path = os.getcwd() + '/static/images'
    if request.method == 'POST':
        
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join(content_path, filename)                     
        file.save(file_path)

        shutil.copy2(file_path, static_path)

        image_path = '/images/' + filename
        print(filename)
        product = classification(file_path)
        print(product)
        
    return render_template('classification.html', product = product, user_image = image_path)

if __name__ == "__main__":
    app.run(debug = True)