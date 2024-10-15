import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/pharma_inventory'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

