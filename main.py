from __future__ import print_function
from flask import Flask, request, render_template, send_from_directory, url_for
from werkzeug.utils import secure_filename
import sys
from FileHandler import *
from Strings import *
from RunGraph import *

app = Flask(__name__)
strings = String()
graph = None

#This route is for the home page
@app.route('/')
@app.route('/index')
def index():
    body = strings.welcome_page_info
    return render_template('welcome.html', name=body)

#This route is for adding a new node to the existing network
@app.route('/add')
def edit():
    return render_template('add_node.html', nodes = graph.nodes)

#This route is for processing user input when wanting to add a new node
@app.route('/add', methods=["POST","GET"])
def add():
    if request.method =="POST":
        try:
            parent = request.form['parent']
            from_to = request.form['from_to']
            rel_type =request.form['rel_type']

            new_node = request.form['node_name']
            type = request.form['type']
            cost = request.form['cost']
            delay = request.form['delay']

            new_node_obj = Node(str(new_node), str(type))

            if from_to == 'from':
                graph.nodes[str(parent)].add_edge(new_node_obj.ID, cost, delay, rel_type)
                print('FROM done')
            else:
                new_node_obj.add_edge(graph.nodes[str(parent)].ID, cost, delay, rel_type)
                print("Not from")

            #graph.nodes[new_node] = new_node_obj
            #now write this node to the json file so that it can be drawn on the graph
            graph.add_node(new_node_obj)
            return render_template('graph.html', nodes=[nodes for nodes in graph.nodes])
        except Exception as e:
            raise

#This route renders the remove node UI
@app.route('/remove')
def remove():
    return render_template('remove.html', nodes = [nodes for nodes in graph.nodes])

#This route is for removing a node from the network
@app.route('/remove', methods=["POST","GET"])
def remove_node():
    if request.method =="POST":
        node = request.form['source'] #check this
        global graph
        for item in graph.nodes:
            if item == str(node):
                del graph.nodes[item]
                return render_template('graph.html',results='Removed node '+node+'successfully.', nodes=[nodes for nodes in graph.nodes])

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
            create_graph(upload.filename)
            nodes = [nodes for nodes in graph.nodes]
            return render_template('graph.html', body="<div id='graphHolder'></div>", nodes=nodes)
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
        search_results = graph.get_results(source_node, destination)
        try:
            path = search_results['path']
            cost = search_results['cost']
            return render_template('graph.html', path=path, cost=cost, nodes=[nodes for nodes in graph.nodes])
        except:
            #Either no path or there has been a validation of rules
            return render_template('graph.html', results=search_results, nodes=[nodes for nodes in graph.nodes] )

    else:
        global graph
        return render_template('graph.html',nodes=[nodes for nodes in graph.nodes])

def create_graph(filename):
    global graph
    graph = RunGraph(filename)
    return graph

@app.route('/graphs')
def graph():
    send_from_directory('static','testFile.json')
    return render_template('graph.html')
