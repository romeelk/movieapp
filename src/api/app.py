#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

movies = [
    {
        'id': 1,
        'title': u'Python returns',
        'year':u'2012',
        'description': u'The revenge of Python', 
        'director': 'James Smith'
    },
    {
        'id': 2,
        'title': u'The Python Chronicles',
        'year':u'2018',
        'description': u'The journey to Python', 
        'director': 'Tom Jones'
    },
    {
        'id': 3,
        'title': u'The Python strikes back',
        'year':u'2019',
        'description': u'The saga continues', 
        'director': 'Tom Jones'
    }
]

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'movies': movies})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)