from flask import Flask
from .models import DB

def create_app():
	'''Create and configurate an instance of the Flask application'''
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
	DB.init_app(app)

	@app.route('/')
	def root():
		return 'Hello Twityoff!'

	return app