import os

class Config(object):
    SQLALCHEMY_DATABASE_URI ='postgres://opraolckukympt:596be618ea3f7d54453ec76e370eb42784267517e444f0f1101ea689c2a65f00@ec2-23-21-186-85.compute-1.amazonaws.com:5432/d34lf0kv2gg0ik'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    S3_BUCKET = "omaidnadiflask"
    S3_KEY = "AKIASTGSYCSJAHNSJR65"
    S3_SECRET = "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"
    S3_LOCATION ='http://s3.us-east-2.amazonaws.com/omaidnadiflask'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    SECRET_KEY = "hello"