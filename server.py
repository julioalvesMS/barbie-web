from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def DefaultCodeSubmissionPage():
    return app.send_static_file('home.html')

@app.route('/submit', methods=['POST'])
def BarbieSubmissionPage():
    
