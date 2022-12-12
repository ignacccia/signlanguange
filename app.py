import fnmatch
from flask import Flask, render_template, request
import sklearn
import numpy as np
import os
from matplotlib import image, pyplot as plt
from pyexpat import model

app = Flask(__name__, template_folder='template')

ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT

def classification(img):

        img = target_size= (128,128)
        imgplot = plt.imshow(img)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis =0)

        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)


        print(fnmatch)
        class_list = os.listdir("/content/Indian")
        
        for j in range(42):
            if classes[0][j] == 1. :
                print("ini adalah gambar : ", class_list[j])
            break

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['GET','POST'])
def predict():
    
    if request.method == 'POST':
        
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join(r'C:/Users/CIA/Downloads/Klasifikasi Bahasa Isyarat/bahasaisyarat/content/', filename)                     
        file.save(file_path)
        print(filename)
        product = classification(file_path)
        print(product)
        
    return render_template('predict.html', product = product, user_image = file_path) 

if __name__ == "__main__":
    app.run(debug = True)