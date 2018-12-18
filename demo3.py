from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
import sqlite3
from flask import g
import json
import re

app = Flask(__name__)

DATABASE = './test_demo_7.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/getData', methods=['GET', 'POST'])
def getData():
    cursor = get_db().cursor()
    cursor.execute( 'select * from COMPANY' )
    values = cursor.fetchall()
    print(values)
    print( type('runoob') )
    print( type( values ) )
    python2json = {}
    python2json["listData"] = values
    print( type( python2json ) )
    print( type( json.dumps(python2json)  ) )
    print( type( str(python2json)  ) )
    return json.dumps(python2json)
    # return str(python2json)

@app.route('/getStr', methods=['GET', 'POST'])
def getStr():
    cursor = get_db().cursor()
    cursor.execute( 'select * from COMPANY' )
    values = cursor.fetchall()
    python2json = {}
    python2json["listData"] = values
    return str(python2json)


@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Bad Request</h1>', 400

# @app.route('/session', methods=['GET', 'POST']) 
# def index():
# form = NameForm()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'))

@app.route('/form', methods=['GET'])
def form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/user', methods=['GET'])
def user():
    return render_template('./user.html')

@app.route('/wrong')
def wrong():
    return abort(404)

@app.route('/redirect')
def redirect():
    return redirect('www.baidu.com')

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer-11', '4r2')
    response.set_cookie('answer-12', '42rrr')
    return response

@app.route('/user_agent',methods=['GET'])
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/name', methods=['GET', 'POST'])
def home():
    return '{"name":"my_name","age":23,"year":2018}'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        print(request.form['username'])
        print(request.form['password'])
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/signup', methods=['GET'])
def signup_form():
    return '''<form action="/signup" method="post">
              <h6><input name="username"></h6>
              <h6><input name="password" type="password"></h6>
              <h6><button type="submit">Sign In</button></h6>
              </form>'''

@app.route('/signup', methods=['POST'])
def signup():
    # 需要从request对象读取表单内容：
    # if request.form['username']=='admin' and request.form['password']=='password':
    #     print(request.form['username'])
    #     print(request.form['password'])
    #     return '<h3>Hello, admin!</h3>'
    res_username = re.match(r'^[0-9a-z]+$', request.form['username'])
    res_password = re.match(r'^[0-9a-z]+$', request.form['password'])
    if res_username and res_password:
        return '<h3>you are number</h3>'
    return '<h3>you are not number</h3>'

if __name__ == '__main__':
    app.run()