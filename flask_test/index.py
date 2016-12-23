from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Welcome Tiny!'


@app.route('/about')
def about():
	return 'Flask build WebSite Test'

@app.route('/user/<username>')
def show_user(username):
	return 'User Name is {}'.format(username)

if __name__ == '__main__':
	app.run()