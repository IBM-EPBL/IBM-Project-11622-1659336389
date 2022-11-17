from cloudant.client import Cloudant
from flask import Flask, render_template, app, request, url_for, redirect


from detect import my_database
client = Cloudant.iam("3a17a3f9-3c07-4117-9b52-fa8c1faf3c24-bluemix","bMA1TdiuS2onmeStqPDpvL6_XCncHBRvO5cpWL9sldSW", connect=True)
my_database = client.create_database('my_database')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index.html')
def home():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/after_reg', methods=['post'])
def after_reg():
    x = [x for x in request.form.values()]
    print(x)
    data = {
        'name': x[0],
        'psw': x[1]
    }
    print(data)
    query = {'name': {'$eq': data['name']}}

    docs = my_database.get_query_result(query)
    print(docs)

    print(len(docs.all()))

    if len(docs.all()) == 0:
        url = my_database.create_document(data)
        # response = requests.get(url)
        return render_template('register.html', pred="Registration Successful, please login using your details")
    else:
        return render_template('register.html', pred="You are already a member, please login using your details")


@app.route('/login')
def login():
    return render_template('login.htmL')


@app.route('/after_login', methods=['POST'])
def after_login():
    user = request.form['name']
    passe = request.form['psw']
    print(user, passe)

    query = {'name': {'$eq': user}}
    docs = my_database.get_query_result(query)
    print(docs)

    print(len(docs.all()))

    if len(docs.all()) == 0:
        return render_template('login.html', pred="The username is not found.")
    else:
        if user == docs[0][0]['name'] and passe == docs[0][0]['psw']:
            return render_template('index.html')
        else:
            print('Invalid User')





if __name__ == '__main__':
    app.run()

