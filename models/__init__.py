#!/usr/bin/python3

"""
This module initializes the storage variable with an
instance of FileStorage class and reloads the data.
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
