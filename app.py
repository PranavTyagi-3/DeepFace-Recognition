from flask import Flask, render_template,request, send_from_directory
import os
from deepface import DeepFace

app=Flask(__name__)
app.secret_key="53CR3T_K3Y"

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
UPLOAD_FOLDER = "static/uploads"
REGISTER_FOLDER = "static/registered"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def new(user_id):
    for root, dirs, files in os.walk(REGISTER_FOLDER):
        for file in files:
            if file.split("_")[0]==user_id:
                return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        uploaded_file = request.files['file']
        name=request.form['name']
        user_id=request.form['user_id']
        if uploaded_file and allowed_file(uploaded_file.filename) and new(user_id):
            fname = os.path.join(REGISTER_FOLDER, user_id+"_"+name)
            uploaded_file.save(fname)
            try:
                result = DeepFace.analyze(fname, actions=['detection'])
            except:
                result = ""
            print(result)
            if result:
                return render_template('register.html',message="Registered Successfully")
            else:
                os.remove(fname)
                return render_template('register.html',message="Unsuccessfull")
        else:
            return render_template('register.html',message="UserId already registered or not correct file type")
    return render_template('register.html')

@app.route('/recognize',methods=["GET","POST"])
def recognition():
    if request.method=="POST":
        uploaded_file = request.files['file']
        fname = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(fname)
        if uploaded_file and allowed_file(uploaded_file.filename):
            verified = recognize(fname)
            if verified:
                return render_template('recognize.html',verify="Success",name=verified[1])
            else:
                return render_template('recognize.html',verify="Fail")
        else:
            return render_template('recognize.html',verify="Wrong file type")
    return render_template('recognize.html')

def recognize(uploaded_file):
    for root, dirs, files in os.walk(REGISTER_FOLDER):
        for file in files:
            registered_image_path = os.path.join(root, file)
            try:
                result = DeepFace.verify(uploaded_file, registered_image_path, model_name="Facenet")
                print(result)
            except:
                result=""
            if result:
                if result['verified']==True:
                    return registered_image_path.split("_")
                else:
                    pass
    return False
    

if __name__ == '__main__':
    app.run()