import os
import json
import random

os.environ['DATABASE'] = ":memory:"

import pytest
from peewee import SqliteDatabase

from jsninjify import create_app
from jsninjify.models import Descriptive, Buzzword, Word

[pytest]
pythonpath = "."

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    
    database = SqliteDatabase()
    database.drop_tables([Descriptive, Buzzword, Word])
    database.create_tables([Descriptive, Buzzword, Word])

    Buzzword.create([{"buzzword": "buzz"}, {"buzzword": "buzz1"}])

    words = [
        {"word": "word"},
        {"word": "word1"},
        {"word": "word2"},
        {"word": "word3"},
        {"word": "word4"},
        {"word": "word5"}
    ]

    Word.insert_many(words).execute()

    descriptives = [
        {"buzzword_id": 1, "word_id": 1},
        {"buzzword_id": 1, "word_id": 2},
        {"buzzword_id": 1, "word_id": 3},
        {"buzzword_id": 1, "word_id": 4},
        {"buzzword_id": 1, "word_id": 5},
        {"buzzword_id": 2, "word_id": 6},
    ]

    Descriptive.insert_many(descriptives).execute()
    
    yield app

    database.create_tables([Descriptive, Buzzword, Word])

@pytest.fixture
def client(app):
    return app.test_client()
