from flask import Flask, render_template, url_for, request, flash
import os 
from dotenv import load_dotenv

load_dotenv() 

menu = {
    'Главная': '/home',
    'О нас': '/about'
}

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('secret_key')


@app.route("/home/")    
def home():
    return render_template('index.html', menu=menu, title = 'Главная')

@app.route("/<int:id>")
def id_1(id):
    return render_template('about.html', username=id)



@app.route("/about")
def about():
    return render_template('about.html', title = 'О нас', menu=menu)

@app.route('/sign_in', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        if (len(request.form)!=3):
            FIO = request.form['Username']
            TEL = request.form['TEL']
            DATE_BIRTH = request.form['Password']
            print(FIO, TEL, DATE_BIRTH)
            flash(message='Данные Отправлены!', category='success')
        else:
            flash(message='Ошибка отправки!', category='error')

    return render_template('sign_in.html', title='Форма входа')


# with app.test_request_context():
#     print(url_for('home'))
#     print(url_for('index', username='B1zn3'))

if __name__ == '__main__':
    app.run(debug=True)
    
