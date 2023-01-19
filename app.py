from flask import Flask,jsonify,request, render_template
import time
from flask_mysqldb import MySQL

app = Flask(__name__)

# Ex01: je créé une route et j'ecris des informations sur le décorateur
# @app.route('/')
# def home():   
#     return ("Done! i grab some information and display it on the decorator!")
# Ex02 : je passe en debug mode

# Ex03 : je créé le lien avec la bdd MySQL
app.config['MYSQL_HOST'] = 'localhost' # je configure flask_mysqldb
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)  # j'initialise flask_mysqldb
# mysql.init_app(app)
@app.route('/', methods=['GET', 'POST'])   
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        cursor = mysql.connection.cursor() # je créé le cursor dans ma fonction
        cursor.execute("INSERT INTO users (username, email) VALUES(%s,%s)",(username,email)) #j'exécute une requête
        mysql.connection.commit()
        # fetchdata = cursor.fetchall() #je récupère les données
        cursor.close()
        return "success"
    return render_template('index.html')

@app.route('/users')
def users():
    cursor = mysql.connection.cursor()
    users = cursor.execute("SELECT * FROM users")

    if users > 0:
        userDetails = cursor.fetchall()
        return render_template('users.html', userDetails=userDetails)


if __name__ == '__main__':
    app.run(debug=True)

# exemple
# @app.route('/greetings')
# def  say_hi():
#     return "Hi there! it's : " + str(time.time())
    # toto = jsonify(key1="toto")
    # return toto

# def do_the_login():
#     return "i'm going to log"

# def show_the_login_form():
#     return "it's over"

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()


# @app.post('/route_name')
# def test():
#     return "Post"

# @app.get('/route_name')
# def testo():
#     return "Get"