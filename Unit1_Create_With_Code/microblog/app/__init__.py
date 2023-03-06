from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

print("test")
print(Config.SQLALCHEMY_DATABASE_URI)

app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "long_secret_key"

db = SQLAlchemy(app)
migrate = Migrate(app,db)


from app import routes, models