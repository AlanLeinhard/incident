from flask import Flask
from werkzeug.serving import run_simple

app = Flask(__name__)
# включаем режим отладки в приложении
app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # передаем аргумент use_debugger=True
    run_simple('localhost', 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)