from maria_db_settings import MariaDbSettings
from maria_db_context import MariaDbContext
import os


def build() -> MariaDbContext:
    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    port = int(os.environ.get('DB_PORT'))
    database = os.environ.get('DB_NAME')

    settings = MariaDbSettings(
        user=user,
        database=database,
        password=password,
        host=host,
        port=port
    )
    context = MariaDbContext(settings)
    return context
