from flask import Flask
app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

app.config.from_envvar('APP_CONFIG_FILE')

app = Flask(__name__)

@app.route('/')
def index():
	return '<h2>O + E = ❤</h2>'
	
if __name__ == "__main__":
	app.run()