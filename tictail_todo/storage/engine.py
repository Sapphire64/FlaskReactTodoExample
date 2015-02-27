from pydoc import locate

from tictail_todo import config


STORAGE_ENGINE = locate(config.STORAGE_ENGINE)()