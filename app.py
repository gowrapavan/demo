from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-model')
def run_model():
    result = subprocess.run(
        ["python", "yolov5/detect.py", "--weights", "yolov5/best.pt", "--img", "416", "--conf", "0.5", "--source", "0"],
        capture_output=True,
        text=True
    )
    return result.stdout  # Sends output to frontend

def handler(event, context):
    return app(event, context)  # Required for serverless deployment
