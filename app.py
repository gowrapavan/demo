from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_detection')
def start_detection():
    # Run `run.py` as a separate process
    subprocess.Popen(["python", "run.py"], shell=True)
    return "Detection started!"

if __name__ == "__main__":
    app.run(debug=True)
