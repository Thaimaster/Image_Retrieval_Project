import numpy as np
from Feature_Extractor import FeatureExtractor
from datetime import datetime
import os
import faiss
from tensorflow.keras.preprocessing import image as kimage
from PIL import Image

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, url_for, render_template, request, redirect, session
# from flask_ngrok import run_with_ngrok

from IVFPQ_Faiss_Search import load_index

# Read image features
fe = FeatureExtractor()

folder_query = "query_pic/"
# root_fearure_path = "static/feature/all_feartures.npz"

# data = np.load(root_fearure_path)
# paths_feature = data["array1"]
# imgs_feature = data["array2"]
static_img_path_dir = "static_img_paths.npz"
img_paths_data = np.load(static_img_path_dir)
img_paths = img_paths_data["array1"]


app = Flask(__name__)
# run_with_ngrok(app)
app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html', mess ="")
    else:
        name = request.form['username']
        passw = request.form['password']

        data = User.query.filter_by(username=name, password=passw).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            # tài khoản sai
            return render_template('login.html', mess= "nhap sai account")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        new_user = User(
            username=request.form['username'],
            password=request.form['password'])

        users = User.query.all()
        for user in users:
            if user.username == new_user.username:
                # username da ton tai
                return render_template('register.html', mess= "username da ton tai")

        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    else:
        return render_template('register.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    
    index = load_index()
    try:
        if session['logged_in'] == False:
            return redirect(url_for('login'))
    except Exception:
        return redirect(url_for('login'))


    if request.method == 'POST':
        file = request.files['query_img']

        # Save query image
        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + file.filename
        img.save(uploaded_img_path)
        
        # Load query image and FeatureExtractor
        #query = kimage.load_img(uploaded_img_path, target_size=(224, 224))
        #query = kimage.img_to_array(query, dtype=np.float32)
        #query = Image.open(uploaded_img_path)
        xq = fe.extract(img).reshape(1,-1)

        # retrieval_images
        k=50
        dist, I = index.search(xq, k)
        img_src = np.array([img_paths[i] for i in I[0]])
        scores = np.array([dist[0], img_src]).T
        # print(scores.shape)
        # print(scores.shape)
        # print(scores[0:5])

        return render_template('index.html',
                               query_path = uploaded_img_path,
                               scores1=scores[:10],
                               scores2=scores[10:20],
                               scores3=scores[20:])

    return render_template('index.html')


if __name__=="__main__":
    # app.run(host='192.168.1.34', port='6868', debug=False)
    app.run(host='localhost', port='6868', debug=False)
    # app.run()
