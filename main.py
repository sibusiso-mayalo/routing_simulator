from flask import Flask, request, render_template, send_from_directory, url_for
from werkzeug.utils import secure_filename
from FileHandler import *
from Strings import *
from RunGraph import *

app = Flask(__name__)
strings = String()

#This route is for the home page
@app.route('/')
@app.route('/index')
def index():
    body = strings.welcome_page_info
    return render_template('welcome.html', name=body)

#This route is for adding a new node to the existing network
@app.route('/edit')
def edit():
    body = 'Add data body'
    return render_template('addData.html', body=body)

#this route renders the form to upload the dataset
@app.route('/upload')
def handle_upload():
    return render_form()

#This route handles the uploaded data set
@app.route('/sendFile', methods=["POST","GET"])
def sendFile():
    response=''
    acceptable_extensions = ['csv','txt','xls']
    if request.method == "POST":
        render_form()
        upload = request.files['file']
        file_handler = FileHandler(secure_filename(upload.filename))

        if file_handler.validate_file():
            upload.save(secure_filename(upload.filename))
            return render_template('graph.html', body="<div id='graphHolder'></div> ")
        else:
            response = 'The file you have uploaded is not supported'
    else:
        response = 'File not uploaded'
    return response

def render_form():
    return render_template('upload_form.html', form = strings.form)

@app.route('/graph', methods=["POST"])
def get_nodes():
    if request.method =="POST":
        source_node = request.form['source']
        destination = request.form['destination']

        search_results = RunGraph.get_results(source_node, destination)
        if type(search_results) == 'dict()':
            path = search_results['path']
            cost = search_results['cost']
            # send to JS to be displayed

        else:
            #Either no path or there has been a validation of rules
            #send validation error message to UI
            print ""

@app.route('/graph')
def graph():
    send_from_directory('static','testFile.json')
    return render_template('graph.html')
