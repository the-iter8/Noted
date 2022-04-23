import os

# absolute path of application
basedir = os.path.abspath(os.path.dirname(__file__))

# Key Environment Variable
keyEnvVar = "SECRET_KEY"

# Database URI Environment Variable
devDbEnvVar = "DEV_DATABASE_URI"
testDbEnvVar = "TEST_DATABASE_URI"
prodDbEnvVar = "DATABASE_URI"


class Config:
    SECRET_KEY = os.getenv(keyEnvVar, "defaultKey")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True;
    SQLALCHEMY_DATABASE_URI = os.getenv(devDbEnvVar) or \
        "sqlite:///" + os.path.join(basedir, 'data_dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True;
    SQLALCHEMY_DATABASE_URI = os.getenv(testDbEnvVar)

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv(prodDbEnvVar)
    SQLALCHEMY_DATABASE_URI = os.getenv(devDbEnvVar) or \
        "sqlite:///" + os.path.join(basedir, 'data.sqlite')


config = {
    "development" : DevelopmentConfig,
    "testing" : TestingConfig,
    "production" : ProductionConfig,
    "default" : Config
}

