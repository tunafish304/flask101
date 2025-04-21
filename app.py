from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.jinja_env.cache = {}
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    # When doing a query, display each row represented 
    # by an object containing what's in the return statement
    def __repr__(self):
        return 'Comment ' + str(self.id)
    
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comments', methods=['POST', 'GET'])
def comments():
    if request.method == 'POST':
        db.session.add(Data(
            comment=request.form['comment'],
        ))
        db.session.commit()
        return redirect('/comments')
    # Get all the comments from the Database
    # This only happens if the method is GET (like and "else")
    comments = Data.query.all()
    return render_template('comments.html', comments=comments)

@app.route('/comments/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    comment_obj = Data.query.get(id)
    if request.method == 'POST':
        comment_obj.comment = request.form['comment']
        db.session.commit()
        return redirect('/comments')
    else:
        return render_template('edit.html', comment=comment_obj)

@app.route('/comments/delete/<int:id>')
def delete(id):
    comment_obj = Data.query.get(id)
    db.session.delete(comment_obj)
    db.session.commit()
    return redirect('/comments')
if __name__ == '__main__':
    app.run(debug=True)