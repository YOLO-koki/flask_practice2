from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # データベースのデータを全部取得
        posts = Post.query.all()
        return render_template('index.html', posts_name=posts)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        
        # 値を新規で生成
        post = Post(title=title, body=body)
        
        # 追加
        db.session.add(post)
        
        # 反映
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create.html')
    
@app.route('/<int:id>/update', methods=['POST', 'GET'])
def update(id):
    # 指定したIDのデータのみ取得
    post = Post.query.get(id)
    
    if request.method == 'GET':
        return render_template('update.html', post_name=post)
    else:
        post.title = request.form.get('title')
        post.body = request.form.get('body')
        
        db.session.commit()
        return redirect('/')
    
@app.route('/<int:id>/delete', methods=['GET'])
def delete(id):
    # 指定したIDのデータのみ取得
    post = Post.query.get(id)
    
    # 削除
    db.session.delete(post)
    
    # 反映
    db.session.commit()
    return redirect('/')
    