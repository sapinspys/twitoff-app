import uuid
from flask import Flask, render_template
from .models import DB, Users, Tweets

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    DB.init_app(app)

    # You can add any HTML/CSS to this
    # We can also add a test user like so:
    # rand_name = str(uuid.uuid4)
    # rand_user = User(name=rand_name)
    # DB.session.add(rand_u)
    # DB.session.commit()
    
    @app.route('/')
    def root():
        return render_template('base.html', title='Hello Page')

    return app

    # DB.drop_all(), drops all tables
    # DB.create_all(), creates all tables, not needed with the above?
    # u1 = Users(name = "something")
    # t1 = Tweets(text = "some text")
    # t2 = Tweets(text = "some other text")
    # u1.tweets.append(t1)
    # u1.tweets.append(t2)
    # DB.session.add(u1)
    # DB.session.commit()