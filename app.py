from flask import Flask
from flask_cors import CORS

from static.Read_csv import Read_csv_create_wordcloud

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cloud', methods=['GET'])
def create_wordcloud_using_csv():
    print('되나')
    C = Read_csv_create_wordcloud()
    result = C.read()
    print(result)
    return result

CORS(app)
if __name__ == '__main__':
    app.run()
