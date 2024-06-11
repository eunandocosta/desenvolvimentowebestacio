from flask import Flask, g, Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from controllers.MediaController import media_blueprint
from controllers.MediaContentController import media_content_blueprint


app = Flask(__name__)

# Create the SQLAlchemy engine
engine = create_engine('sqlite:///media.db')  # Adjust the URL as necessary

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Your blueprint setup
app.register_blueprint(media_blueprint, url_prefix='/media')
app.register_blueprint(media_content_blueprint, url_prefix='/media_content')


# Fornece a sessão para as rotas
@app.before_request
def create_session():
    g.session = Session()

@app.teardown_request
def remove_session(exception=None):
    session = g.pop('session', None)
    if session is not None:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)
