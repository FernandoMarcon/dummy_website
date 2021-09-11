import os

class Config(object):
    # python3 -c "import os; print(os.urandom(16))" -> secret_string
    SECRET_KEY = os.environ.get('SECRET_KEY') or "P\xfa\x9fq\xc1\xe6i(\x14\xae\xcf2\x9c\xd1\x7fx"

    MONGODB_SETTINGS = {'db':'UTA_Enrollment'}
