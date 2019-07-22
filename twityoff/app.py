from flask import Flask

def create_app():
	'''Create and configurate an instance of the Flask application'''
	app = Flask(__name__)

	@app.route('/')
	def root():
		return 'Hello Twityoff!'

	return app