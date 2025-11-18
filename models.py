from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

# create connection start into your database
db = create_engine('sqlite:///banco.db')

# create a data base
Base = declarative_base()

# create the class/tables of data base
class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String)
    email = Column('email', String, unique=True)
    password = Column('password', String)
    active = Column('active', Boolean, default=True)
    admin = Column('admin', Boolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin

class Order (Base):
    __tablename__ = 'order'

    # STATUS_PENDING = (
    #     ("PENDING", "PENDING"),
    #     ("IN_PROGRESS", "IN_PROGRESS"),
    #     ("DONE", "DONE"),
    # )

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    # status = Column('status', ChoiceType(STATUS_PENDING)) Se enviar assim retorna um erro no alembic
    status = Column('status', String)
    user = Column('user', ForeignKey('users.id'))
    price = Column('price', Float)
    # items 

    def __init__(self, user, status="PENDING", price=0):
        self.user = user
        self.status = status
        self.price = price

class ItemsOrder (Base):
    __tablename__ = 'items_order'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    quantity = Column('quantity', Integer)
    flavor = Column('flavor', String)
    size = Column('size', String)
    unit_price = Column('unit_price', Float)
    order = Column('order', ForeignKey('order.id'))

    def __init__(self, unit_price, quantity, flavor, size, order):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unit_price = unit_price
        self.order = order

# execute the create metadata
# Base.metadata.create_all(db)