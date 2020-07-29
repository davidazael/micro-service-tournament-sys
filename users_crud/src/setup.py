from pprint import pformat
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
    log.info(pformat('Created database {}'.format(base.db_name), indent=2))
    base.Base.metadata.drop_all(base.engine)
    base.Base.metadata.create_all(base.engine)
    log.info(pformat('Table users DESC: {}'.format(base.Base.metadata.tables),
        indent=2))

    log.info('Inserting User Data')
    with open('database/data/users.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            user = ModelUsers(**record)
            base.db_session.add(user)
        base.db_session.commit()
