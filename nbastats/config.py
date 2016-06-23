class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/nbastats"
    DEBUG = True
    UPLOAD_FOLDER = "uploads"

class TestingConfig(object):
    DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/nbastats-test"
    DEBUG = True
    UPLOAD_FOLDER = "test-uploads"
