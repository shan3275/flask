from flask import Flask,request
from flask import render_template, redirect,url_for, send_file, send_from_directory

app = Flask(__name__, template_folder="templates/html",static_folder="templates/html",static_url_path="")

@app.route('/')
def index():
        return render_template("back.html")

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/cookie')
def show_cookie_profile():
    # show the user profile for that user
    return 'ip %s' % request.args.get('ip')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/post/<float:post_id>')
def show_post1(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %f' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
