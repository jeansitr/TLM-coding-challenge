import json
from re import L
from flask import jsonify
from peewee import Model

class BaseModel(Model):
    class Meta:
        database = ""

class Buzzword(BaseModel):
    id = AutoField(primary_ky=True)
    buzzword = CharField(nill=False, unique=True)
    
class Word(BaseModel):
    id = AutoField(primary_ky=True)
    Word = CharField(nill=False, unique=True)

class Descriptive(BaseModel):
    buzzword_id = ForeignKeyField(Buzzword, to_field="id")
    word_id = ForeignKeyField(Word, to_field="id")

    class Meta:
        primary_key = CompositeKey('buzzword_id', 'word_id')
