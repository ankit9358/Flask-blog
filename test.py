from flask import Flask,render_template,request,session,redirect
from  flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
from werkzeug.utils import secure_filename
import json,os,math

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = params['upload_location']

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)
mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']


db = SQLAlchemy(app)


class Contacts(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    sub_tittle =db.Column(db.String(80),nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(20), nullable=True)



@app.route("/home")
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts) / int(params['no_of_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['no_of_posts']): (page - 1) * int(params['no_of_posts']) + int(
        params['no_of_posts'])]
    if (page == 1):
        prev = "#"
        next = "/home?page=" + str(page + 1)
    elif (page == last):
        prev = "/home?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/home?page=" + str(page - 1)
        next = "/home?page=" + str(page + 1)
    return render_template('home.html', params=params, posts=posts, prev=prev, next=next,page=page,last=last)


@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, msg = message, date= datetime.now(),email = email )
        db.session.add(entry)
        db.session.commit()
        try:
            mail.send_message('New message from ' + name,
                              sender=email,
                              recipients=[params['gmail-user']],
                              body=message + "\n" + phone
                              )
        except:
            return 'Check Your Connection and Reload'
    return render_template('contact.html', params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if session.get('user'):
        if request.method == "POST":
            tittle = request.form.get('tittle')
            subtittle = request.form.get('subtittle')
            slug = request.form.get('Slug')
            content = request.form.get('content')
            img = request.files['file_img']
            img_fil =  os.path.join(img.filename)
            date = datetime.now()
            if sno == '0':
                post = Posts(tittle=tittle,slug=slug,content=content,sub_tittle=subtittle,date= date,img_file=img_fil)
                img.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(img.filename)))
                db.session.add(post)
                db.session.commit()
            else:
                posts = Posts.query.filter_by(sno=sno).first()
                posts.tittle = tittle
                posts.sub_tittle = subtittle
                posts.slug = slug
                posts.content = content
                posts.date = datetime.now()
                if img_fil == "":
                    img.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(posts.img_file)))
                else:
                    posts.img_file = img_fil
                    img.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(posts.img_file)))
                db.session.commit()
                return redirect('/login')
        posts = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, posts=posts, sno=sno)
    else:
        return redirect('/home')



@app.route("/login", methods = ['GET', 'POST'])
def login():
    if not session.get('user'):
        if request.method == "POST":
            user = request.form.get('userid')
            pwd = request.form.get('passwd')
            if user == params['username'] and pwd == params['password']:
                session['user'] = user
                posts = Posts.query.filter_by().all()[0:params['no_of_posts']]
                return render_template('dashboard.html',params=params, posts=posts)
            else:
                msg = 'Invalid Username/Password'
                cont = {'message': msg}
                return render_template('login.html', cont)

        return render_template('login.html', params=params)
    else:
        posts = Posts.query.filter_by().all()[0:params['no_of_posts']]
        return render_template('dashboard.html', params=params, posts=posts)

@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    try:
        session.pop('user', None)
        return redirect('/login')
    except:
        return redirect('/login')

@app.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if session.get('user'):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/login')




app.run(debug=True)
