import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Storage selection
STORAGE_ENGINE = \
    'tictail_todo.storage.inmemory_dict.InMemoryDictToDoStorageProvider'