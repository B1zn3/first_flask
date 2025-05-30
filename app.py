from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/home/")
def home():
    return render_template('index.html')

@app.route("/<string:username>")
def index(username):
    return render_template('index.html', title='Главная', name=username)

# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for('index', username='B1zn3'))

if __name__ == '__main__':
    app.run(debug=True)
    
