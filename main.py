from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename
from FileHandler import *
app = Flask(__name__)


#This route is for the home page
@app.route('/')
@app.route('/index')
def index():
    body = 'This is the body of the HTML'
    return render_template('welcome.html', name=body)

#This route is for adding a new node to the existing network      
@app.route('/edit')
def edit():
    body = 'Add data body'
    return render_template('addData.html', body=body)

#this route renders the form to upload the dataset
@app.route('/uploadData')
def handle_upload():
    return render_form()

#This route handles the uploaded data set
@app.route('/sendFile', methods=["POST","GET"])
def sendFile():
    lines = str()
    acceptable_extensions = ['csv','txt','xls']
    if request.method == "POST":
        render_form()
        upload = request.files['file']
        
        file_handler = FileHandler(secure_filename(upload.filename))
        if file_handler.validate_file():
            upload.save(secure_filename(upload.filename))
        
            with open(secure_filename(upload.filename),"r") as line:
                lines+= "\n <br>"+line.read()+"</br>"
        else:
            lines = 'The file you have uploaded is not supported' 
    return lines      
            
def render_form():

    complete_form = list()
    complete_form.append("<form action='http://localhost:5000/sendFile'")
    complete_form.append(" method=POST enctype=multipart/form-data")
    complete_form.append(" action={{ url_for('sendFile')}}>")
    complete_form.append(" <input type = 'file' name = 'file' /> ")
    complete_form.append(" <input type = 'submit' /> </form>")
    
    return render_template('upload_form.html', form = ''.join(complete_form))
        
