# for production replace 'local' with 'production'
APP_ENV = 'local' 

APP_DEBUG = False if APP_ENV == 'production' else True

DATABASE_NAME = 'indian_banks'
DATABASE_USERNAME = 'postgres'
DATABASE_PASSWORD = 'password'
HOST = '127.0.0.1'

Postgres_URL = 'postgres://tredpdzfxmfaaq:21f5c7c984244ba56b89ee5b0f743376f785c4ccffc15701201b01a0ce191f8a@ec2-23-21-220-32.compute-1.amazonaws.com:5432/dpd3nsi4eaong'
