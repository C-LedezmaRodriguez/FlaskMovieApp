from flask import Flask
from dotenv import load_dotenv
from config import config
from app.routes import bp as main_bp

load_dotenv()
app = Flask(__name__)
app.config.from_object(config['development']) 

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
