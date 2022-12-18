from flask import Flask
from flask import render_template
from flask import request
from flask import Response

from SessionUser import SessionUser
from TestDb import TestDb

app = Flask(__name__)
db = TestDb()

@app.route('/')
def AR_index():  # put application's code here
    return render_template('index.html', user=db.getuser(request.cookies.get('session')))

@app.route('/lists')
def AR_lists():
    user = db.getuser(request.cookies.get('session'))
    errors = []
    if not user.logged_in:
        errors = ['Du musst eingeloggt sein um deine Listen zu sehen']
    return render_template('lists.html', user=user, lists=db.getlists(user), errors=errors)

@app.route('/list')
def AR_list():
    user = db.getuser(request.cookies.get('session'))
    if user.logged_in:
        articles = db.getlist(user, request.args.get('id'))
        if(articles == None):
            return render_template('list.html', user=user, articles=[], errors=['Diese Liste existiert nicht'])
        return render_template('list.html', user=user, articles=articles)
    return render_template('list.html', user=user, articles=[], errors=['Du musst eingeloggt sein um deine Liste zu sehen'])

@app.route('/login')
def AR_login():
    user = db.getuser(request.cookies.get('session'))
    if user.logged_in:
        return b'<meta http-equiv="refresh" content="0; url=lists">'
    return render_template('login.html', user=user)

@app.route('/logout')
def AR_logout():
    return render_template('logout.html', user=db.getuser(request.cookies.get('session')))

@app.route('/register')
def AR_register():
    return render_template('register.html', user=db.getuser(request.cookies.get('session')))

@app.route('/resetpassword')
def AR_resetpassword():
    return render_template('resetpassword.html', user=db.getuser(request.cookies.get('session')))



@app.route('/login', methods=['POST'])
def ARI_login():
    lo = db.login(request.form.get('username'), request.form.get('password'))
    if(lo == None):
        r = render_template('login.html', user=db.getuser(request.cookies.get('session')), errors=['Falscher Benutzer oder Passwort!'])
    else:
        r = Response(b'<meta http-equiv="refresh" content="0; url=lists">')
        r.set_cookie("session", lo)
    return r

@app.route('/logout', methods=['POST'])
def ARI_logout():
    r = Response(b'<meta http-equiv="refresh" content="0; url=login?info=Erfolgreich%20ausgeloggt">')
    r.delete_cookie("session")
    return r

@app.route('/resetpassword', methods=['POST'])
def ARI_resetpassword():
    return b'<meta http-equiv="refresh" content="0; url=login?info=Die%20Anweisungen%20zum%20Passwort%20zur%C3%BCcksetzen%20wurden%20gesendet">'

@app.route('/register', methods=['POST'])
def ARI_register():
    return b'<meta http-equiv="refresh" content="0; url=login?info=Email%20gesendet,%20bitte%20folgen%20Sie%20den%20Anweisungen%20im%20Email">'

if __name__ == '__main__':
    app.run(debug=True)
