import environ

SETTINGS_VARS = {
    'DEBUG': (bool, False)
}

env = environ.Env(**SETTINGS_VARS)
environ.Env.read_env()
default_db = env.db()
