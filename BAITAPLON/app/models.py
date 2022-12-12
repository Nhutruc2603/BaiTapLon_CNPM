# from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text, Enum, DateTime
# from sqlalchemy.orm import relationship, backref
# from app import db, app
# from enum import Enum as UserEnum
# from flask_login import UserMixin
# from datetime import datetime
#
#
# class UserRole(UserEnum):
#     USER = 1
#     ADMIN = 2
#
#
# class BaseModel(db.Model):
#     __abstract__ = True
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#
#
# class Category(BaseModel):
#     __tablename__ = 'category'
#
#     name = Column(String(50), nullable=False)
#     products = relationship('Product', backref='category', lazy=False)
#
#     def __str__(self):
#         return self.name
#
#
# prod_tag = db.Table('prod_tag',
#                     Column('product_id', Integer,
#                            ForeignKey('product.id'), nullable=False, primary_key=True),
#                     Column('tag', Integer,
#                            ForeignKey('tag.id'), nullable=False, primary_key=True))
#
#
# class Product(BaseModel):
#     name = Column(String(50), nullable=False)
#     description = Column(Text)
#     price = Column(Float, default=0)
#     image = Column(String(100))
#     active = Column(Boolean, default=True)
#     category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
#     tags = relationship('Tag', secondary='prod_tag', lazy='subquery',
#                         backref=backref('products', lazy=True))
#     receipt_details = relationship('ReceiptDetails', backref='product', lazy=True)
#     comments = relationship('Comment', backref='product', lazy=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Tag(BaseModel):
#     name = Column(String(50), nullable=False, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class User(BaseModel, UserMixin):
#     name = Column(String(50), nullable=False)
#     username = Column(String(50), nullable=False)
#     password = Column(String(50), nullable=False)
#     avatar = Column(String(100), nullable=False)
#     active = Column(Boolean, default=True)
#     # account_name=Column(String(50),nullable=False)
#     # phone=Column(String(10),nullable=False)
#     # account_number=Column(String(50),nullable=False)
#     # bank_branch=Column(String(50),nullable=False)
#     user_role = Column(Enum(UserRole), default=UserRole.USER)
#     receipts = relationship('Receipt', backref='user', lazy=True)
#     comments = relationship('Comment', backref='user', lazy=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Receipt(BaseModel):
#     created_date = Column(DateTime, default=datetime.now())
#     user_id = Column(Integer, ForeignKey(User.id), nullable=False)
#     details = relationship('ReceiptDetails', backref='receipt', lazy=True)
#
#
# class ReceiptDetails(BaseModel):
#     quantity = Column(Integer, default=0)
#     price = Column(Float, default=0)
#     receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
#     product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
#
#
# class Comment(BaseModel):
#     content = Column(String(255), nullable=False)
#     created_date = Column(DateTime, default=datetime.now())
#     product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
#     user_id = Column(Integer, ForeignKey(User.id), nullable=False)
#
#
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#         c1 = Category(name='Điện thoại')
#         c2 = Category(name='Máy tính bảng')
#         c3 = Category(name='Phụ kiện')
#
#         db.session.add_all([c1, c2, c3])
#         db.session.commit()
#
#         p1 = Product(name='iPhone 13 Pro Max', description='Apple, 256GB', price=35000000,
#                      image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
#                      category_id=1)
#         p2 = Product(name='iPad Pro 2022', description='Apple, 128GB', price=32000000,
#                      image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',
#                      category_id=2)
#         p3 = Product(name='Sạc dự phòng', description='Apple, 16GB', price=24000000,
#                      image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
#                      category_id=3)
#         p4 = Product(name='Galax Fold Z', description='Samsung, 256GB', price=33000000,
#                      image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
#                      category_id=1)
#         p5 = Product(name='Galaxy Note Ultra 2022', description='Samsung, 128GB', price=32000000,
#                      image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',
#                      category_id=1)
#         p6 = Product(name='Apple Watch S7', description='Apple, 16GB', price=24000000,
#                      image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
#                      category_id=3)
#
#         db.session.add(p1)
#         db.session.add(p2)
#         db.session.add(p3)
#         db.session.add(p4)
#         db.session.add(p5)
#         db.session.add(p6)
#
#         db.session.commit()
#
#         import hashlib
#         password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())
#         u = User(name='Thanh', username='admin',
#                  password=password,
#                  user_role=UserRole.ADMIN,
#                  avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg')
#         db.session.add(u)
#         db.session.commit()
#
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text, Enum, DateTime
from sqlalchemy.orm import relationship, backref
from app import db, app
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(50), nullable=False)

    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name


# sân bay
class CatAirport(BaseModel):
    __tablename__ = 'catairport'
    name = Column(String(50), nullable=False)

    products = relationship('Product', backref='catairport', lazy=False)


#     chuyến bay
class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    date_start = Column(String(50), nullable=False)
    date_end = Column(String(50), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    catairport_id = Column(Integer, ForeignKey(CatAirport.id), nullable=False)
    tags = relationship('Tag', secondary='prod_tag', lazy='subquery',
                        backref=backref('products', lazy=True))
    receipt_details = relationship('ReceiptDetails', backref='product', lazy=True)
    start_place = Column(String(50), nullable=False)
    end_place = Column(String(50), nullable=False)

    def __str__(self):
        return self.name


class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    # account_name = Column(String(50), nullable=False)
    # phone = Column(String(10), nullable=False)
    # account_number = Column(String(50), nullable=False)
    # bank_branch = Column(String(50), nullable=False)
    # cart_id = Column(String(12), nullable=False)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    receipts = relationship('Receipt', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = Column(String(50), nullable=False, unique=True)

    def __str__(self):
        return self.name


prod_tag = db.Table('prod_tag',
                    Column('product_id', Integer,
                           ForeignKey('product.id'), nullable=False, primary_key=True),
                    Column('tag', Integer,
                           ForeignKey('tag.id'), nullable=False, primary_key=True))


# hóa đơn
class Receipt(BaseModel):
    created_date = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    details = relationship('ReceiptDetails', backref='receipt', lazy=True)


# chi tiết hóa đơn hóa đơn
class ReceiptDetails(BaseModel):
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)


class Comment(BaseModel):
    content = Column(String(255), nullable=False)
    created_date = Column(DateTime, default=datetime.now())
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        import hashlib

        password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())
        u = User(name='nhutruc', username='admin',
                 password=password,
                 user_role=UserRole.ADMIN,
                 avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg')
        db.session.add(u)
        db.session.commit()

db.create_all()
p1 = Product(name='TP.HCM - Phú Yên',
             description='Máy bay: Airbus A321,Hành lý xách tay:7Kg(56x36x23)cm,Hành lý kí gửi: 0Kg',
             price=40000000,
             date_start='12-12-2022 08:15:00',
             date_end='12-12-2022 13:50:00',
             image='https://huongtientourist.com/wp-content/uploads/2022/04/VNO-Best-Time-To-Visit-Vung-Tau.jpeg',
             start_place='TP.Hồ Chí Minh',
             end_place='Phú Yên',
             category_id=1,
             catairport_id=1
             )
p2 = Product(name='TP.HCM - Quãng Ngãi',
             description='Máy bay: BAMBOO A321,Hành lý xách tay:7Kg(56x36x23)cm,Hành lý kí gửi: <10Kg',
             price=5000000,
             date_start='15-12-2022 08:15:00',
             date_end='15-12-2022 13:50:00',
             image='https://culaochamtourist.vn/wp-content/uploads/2021/07/canh-dep-quang-ngai-3.jpg',
             start_place='TP.Hồ Chí Minh',
             end_place='Quãng Ngãi',
             category_id=2,
             catairport_id=2)

p3 = Product(name='TP.HCM - Thượng Hải',
             description='Máy bay: Boeing 787,Hành lý xách tay:8Kg(56x36x23)cm,Hành lý kí gửi: <10Kg',
             price=7800000,
             date_start='20-12-2022 08:15:00',
             date_end='20-12-2022 13:50:00',
             image='https://dulichchat.com/wp-content/uploads/2019/04/tay-duong-co-tran-dulichchat-6.jpg',
             start_place='TP.Hồ Chí Minh',
             end_place='Thượng Hải',
             category_id=2,
             catairport_id=4)

p4 = Product(name='TP.HCM - HÀN QUỐC',
             description='Máy bay: Boeing 787,Hành lý xách tay:8Kg(56x36x23)cm,Hành lý kí gửi: <10Kg',
             price=5000000,
             date_start='20-12-2022 08:15:00',
             date_end='20-12-2022 13:50:00',
             image='https://dulichchat.com/wp-content/uploads/2019/04/tay-duong-co-tran-dulichchat-6.jpg',
             start_place='TP.Hồ Chí Minh',
             end_place='Hàn Quốc',
             category_id=2,
             catairport_id=5)
p5 = Product(name='TP.HCM - Phú sĩ',
             description='Máy bay: Boeing 787,Hành lý xách tay:8Kg(56x36x23)cm,Hành lý kí gửi: <10Kg',
             price=5000000,
             date_start='20-12-2022 08:15:00',
             date_end='20-12-2022 13:50:00',
             image='http://vnnews24h.net/img_data/images/tim-hieu-nhung-dieu-thu-vi-ve-dat-nuoc-nhat-ban.jpg',
             start_place='TP.Hồ Chí Minh',
             end_place='Hàn Quốc',
             category_id=4,
             catairport_id=6)
p6 = Product(name='Hà Nội - TP.Hồ Chí Minh',
             description='Máy bay: Boeing 787,Hành lý xách tay:8Kg(56x36x23)cm,Hành lý kí gửi: <10Kg',
             price=5000000,
             date_start='20-12-2022 08:15:00',
             date_end='20-12-2022 13:50:00',
             image='http://vnnews24h.net/img_data/images/tim-hieu-nhung-dieu-thu-vi-ve-dat-nuoc-nhat-ban.jpg',
             start_place='Hà Nội ',
             end_place='TP.Hồ Chí Minh',
             category_id=1,
             catairport_id=6)
p7 = Product(name='Cần Thơ - Thanh hóa',
             description='Máy bay: Boeing 787,Hành lý xách tay:8Kg(56x36x23)cm,Hành lý kí gửi: <10Kg',
             price=5000000,
             date_start='15-12-2022 08:15:00',
             date_end='15-12-2022 13:50:00',
             image='https://wiki-travel.com.vn/uploads/picture/anhthuy1202-184230114249-du-lich-can-tho-hoang-hon.jpg',
             start_place='TP.Hồ Chí Minh',
             end_place='Cần Thơ',
             category_id=1,
             catairport_id=3)
p8 = Product(name='TP.HCM - Đức',
             description='Máy bay: Boeing 787,Hành lý xách tay:8Kg(56x36x23)cm,Hành lý kí gửi: <10Kg',
             price=5000000,
             date_start='15-12-2023 08:15:00',
             date_end='15-12-2023 13:50:00',
             image='https://www.vietnambooking.com/wp-content/uploads/2017/01/du-lich-phap-14-10-2017-9.jpg',
             start_place='TP.Hồ Chí Minh',
             end_place='Đức',
             category_id=3,
             catairport_id=4)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.add(p6)
db.session.add(p7)
db.session.add(p8)
db.session.commit()
c1 = CatAirport(name='Thanh Hóa')
c2 = CatAirport(name='Cần Thơ')
c3 = CatAirport(name='Nha Trang')
c4 = CatAirport(name='Đà Nẵng')
c4 = CatAirport(name='SaPa')
c5 = CatAirport(name=' Hà Nội')

c1 = CatAirport(name='Haneda')
c2 = CatAirport(name='Charles de Gaulle')
c3 = CatAirport(name='Franscico')
c4 = CatAirport(name='Delhi')
c5 = CatAirport(name=' Narita (NRT)')
db.session.add_all([c1, c2, c3, c4, c5])
db.session.commit()

c1 = Category(name='Miền Bắc')
c2 = Category(name='Miền Trung')
c3 = Category(name='Miền Nam')
c4 = Category(name='Nước Ngoài')
db.session.add_all([c1, c2, c3, c4])
db.session.commit()

import hashlib

password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())
u = User(name='nhutruc', username='admin',
         password=password,
         user_role=UserRole.ADMIN,
         avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg')
db.session.add(u)
db.session.commit()

db.create_all()
