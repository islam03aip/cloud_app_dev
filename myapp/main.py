from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))
    
def add_task_to_cloud(task):
    url = "our_function_url"
    response = requests.post(url, json={"task": task})
    return response.text

if __name__ == '__main__':
    app.run(debug=True)