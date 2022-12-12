from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
from flask_babelex import Babel
import cloudinary


app = Flask(__name__)
app.secret_key = 'dfghds1245er4343546755645634r34'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@localhost/quanlychuyenbay?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CART_KEY'] = 'cart'

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
babel = Babel(app=app)

cloudinary.config(cloud_name='dnyraj6xr', api_key='865883493826844', api_secret='ols6rs_1yvycr_lDJW32EoPJ_Ic')


@babel.localeselector
def load_locale():
    return 'vi'
