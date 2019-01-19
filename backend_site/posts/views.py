from flask import Blueprint, jsonify

blueprint = Blueprint('posts', __name__)


def makeMockPost(title, content):
    """
    TODO: Posting functionality
    """
    post = dict()
    post['title'] = title
    post['content'] = content
    return post


@blueprint.route('/', methods=['GET'])
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
