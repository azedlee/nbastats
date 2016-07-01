class DevelopmentConfig(object):
    DATABASE_URI = "postgres://zmdkdpsjliuemk:NLy9RzlvAtKyw5OZ50Xn7neP4P@ec2-23-21-148-9.compute-1.amazonaws.com:5432/d3gntcc7ejvold"
    DEBUG = True

class TestingConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/nbastats-test"
    DEBUG = True
