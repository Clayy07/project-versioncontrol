from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

import subprocess

def build_docker_image():
    subprocess.run(['docker', 'build', '-t', 'flask_app', '.'])

def run_docker_container():
    subprocess.run(['docker', 'run', '-d', '-p', '5000:5000', '--name clay_app', 'flask_app'])

if __name__ == "__main__":
    build_docker_image()
    run_docker_container()
    print("program ini  akan berjalan di http://localhost:5000")
