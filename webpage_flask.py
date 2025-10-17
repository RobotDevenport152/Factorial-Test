from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, Flask!</h1>'


@app.route('/username/<username>')
def user_behavior(username):
    return f'<h1>{username} is learning Flask!</h1>'

@app.route('/cal/<int:number>')
def show_square(number):
    return f"The square of {number} is {number**2}"

if __name__ == '__main__':
    app.run(debug=True)
