CONFIG_PATH = "src/infrastructure/config/"
CELERY_CONFIG = 'celeryconfig.py'

# BD
STORAGE_TYPE = "mysql"
MESSAGE_BROKER_TYPE = "rabbitmq"

STORAGE_SQLITE_NAME = "ifome.db"
STORAGE_SQLITE_PATH = f"{CONFIG_PATH}{STORAGE_SQLITE_NAME}"

# MESSAGE_BROKER
BUY_QUEUE = "buy"
HOST_MSG_BROKER = "localhost"
