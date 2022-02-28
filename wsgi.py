from flask import Flask
from app import maan

app = Flask(__name__)
# включаем режим отладки в приложении
app.debug = True


# def hello_world():
#     return 'Hello World!'

@app.route('/')
def main():
    maan()


if __name__ == '__main__':
    # передаем аргумент use_debugger=True
    app.run('localhost', 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)