from ast import literal_eval
from database.model_users import ModelUsers
from database import base
import logging
import sys

# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    log.info('Created database {}'.format(base.db_name))
    base.Base.metadata.create_all(base.engine)
    log.info('Table users DESC: {}'.format(base.Base.metadata.tables))
