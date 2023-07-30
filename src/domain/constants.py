CONFIG_PATH = "src/infrastructure/config/"

# BD
STORAGE_TYPE = "mysql"
STORAGE_SQLITE_NAME = "ifome.db"
STORAGE_SQLITE_PATH = f"{CONFIG_PATH}{STORAGE_SQLITE_NAME}"

# MESSAGE_BROKER
BUY_QUEUE = "buy"
DELIVERY_QUEUE = "delivery"
HOST_MSG_BROKER = "localhost"
MESSAGE_BROKER_TYPE = "rabbitmq"
