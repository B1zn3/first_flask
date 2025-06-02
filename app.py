from flask import Flask, render_template, url_for, request



app = Flask(__name__)



@app.route("/home/")
def home():
    return render_template('index.html')

@app.route("/<int:id>")
def id_1(id):
    return render_template('about.html', username=id)

@app.route("/about/<string:username>")
def about(username):
    return render_template('about.html', title = 'О нас', username=username)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        FIO = request.form['Username']
        TEL = request.form['TEL']
        DATE_BIRTH = request.form['Password']
        print(FIO, TEL, DATE_BIRTH)
    return render_template('register.html', title='Форма регистрации')


# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for('index', username='B1zn3'))

if __name__ == '__main__':
    app.run(debug=True)
    
