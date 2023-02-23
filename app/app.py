import os
import pickle
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return render_template('index.html')

# Define a route to handle file uploads and predictions
@app.route('/predict', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded file and save it to disk
        file = request.files['filename']
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        # file.save(file_path)
        # print(f"File saved to {file_path}")
        # Make a prediction
        img = Image.open(file)
        resize = tf.image.resize(img, (256,256))

        # Load the pre-trained model
        
        loaded_model = load_model('models/imageclassifier.h5')
        prediction = loaded_model.predict(np.expand_dims(resize/255, 0))
        if (prediction.argmax() == 0):
            string = 'Bed'
        elif (prediction.argmax() == 1):
            string = 'Chair'
        elif (prediction.argmax() == 2):
            string = 'Sofa'
        # Return the prediction to the index.html template
        return render_template('index.html', prediction=string)
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)