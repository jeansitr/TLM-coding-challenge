import os
import json
import click
import random

from flask.cli import with_appcontext
from peewee import Model, PostgresqlDatabase, AutoField, CharField, ForeignKeyField, CompositeKey

class BaseModel(Model):
    class Meta:
        database = PostgresqlDatabase(os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))

class Buzzword(BaseModel):
    id = AutoField(primary_key=True)
    buzzword = CharField(null=False, unique=True)
    
class Word(BaseModel):
    id = AutoField(primary_key=True)
    word = CharField(null=False, unique=True)

class Descriptive(BaseModel):
    buzzword_id = ForeignKeyField(Buzzword, to_field="id")
    word_id = ForeignKeyField(Word, to_field="id")

    class Meta:
        primary_key = CompositeKey('buzzword_id', 'word_id')

@click.command("init-db")
@with_appcontext
def init_db_command():
    database = PostgresqlDatabase(os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
    database.drop_tables([Buzzword, Word, Descriptive])
    database.create_tables([Buzzword, Word, Descriptive])

    buzzwords = []
    words = []

    #read json files to populate Database
    with open('jsninjify/json/buzzwords.json') as file:
        data = json.load(file)
        buzzwords = data["buzzwords"]

    with open('jsninjify/json/words.json') as file:
        data = json.load(file)
        words = data["words"]

    #Creating words in database
    for w in words:
        Word.create(word=w)

    #creating buzzwords and associating 5 random words to it
    ind = 1
    for bw in buzzwords:

        Buzzword.create(buzzword=bw)

        #chooses 5 words to associate to the buzzword
        chosen = []
        for i in range(5):
            wordID = random.randrange(1, len(words) + 1)

            #Assures that a word isn't chosen twice
            while wordID in chosen:
                wordID = random.randrange(1, len(words) + 1)
            
            Descriptive.create(buzzword_id = ind, word_id = wordID)
            
            chosen.append(wordID)

        ind += 1

    click.echo("database Initialized.")

def init_app(app):
    app.cli.add_command(init_db_command)