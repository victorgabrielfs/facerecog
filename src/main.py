from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellofacerecog():
    return 'Hello FaceRecog'


app.run()