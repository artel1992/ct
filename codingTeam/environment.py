import environ

SETTINGS_VARS = {
    'DEBUG': (bool, False),
    'ACCESS_TOKEN_LIFETIME': (dict, {'minutes': 10}),
    'REFRESH_TOKEN_LIFETIME': (dict, {'minutes': 30}),
    'EMAIL_HOST': (str, None),
    'EMAIL_PORT': (str, None),
    'EMAIL_HOST_USER': (str, None),
    'EMAIL_HOST_PASSWORD': (str, None),
    'DEFAULT_FROM_EMAIL': (str, None),
    'EMAIL_SUBJECT_PREFIX': (str, None),
    'SERVER_EMAIL': (str, None),
}

env = environ.Env(**SETTINGS_VARS)
environ.Env.read_env()
default_db = env.db()
