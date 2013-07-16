DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'djconf',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'djconf_user',
        'PASSWORD': 'eYSCyg91y3sI7WzMkCpT',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Twilio account information
TWILIO_ACCOUNT_SID = 'AC4e88fb53b55406e0e94d9dbcb21bfa15'
TWILIO_AUTH_TOKEN = 'fd4523cd5017aa77b7c4a85e5ee2328f'

TWILIO_DEFAULT_CALLERID = '12013570863'
