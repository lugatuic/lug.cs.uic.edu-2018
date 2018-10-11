"""
Backend server for LUG@UIC website
"""
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static/', static_folder='frontend-site/dist')

CORS(app)

@app.route('/')
def homePage():
  """
  Route for '/' - Home Page
  """
  return app.send_static_file('index.html')

@app.route('/static/<path:path>')
def sendStatic(path):
  """
  Route for all files under '/static/'
  """
  return app.send_static_file(path)

@app.route('/api')
def appRoot():
  """
  Route for '/api'
  """
  return 'API response here!'

def makeMockPost(title, content):
  """
  TODO: Posting functionality
  """
  post = dict()
  post['title'] = title
  post['content'] = content
  return post

@app.route('/api/posts')
def getPosts():
  """
  API function to retrieve all posts
  """
  posts = [
    makeMockPost('Test post', 'Test post. Please Ignore'),
    makeMockPost('First post', 'This is the first, non-test post'),
    makeMockPost('Foo?', 'Bar.'),
  ]
  return jsonify(posts)

