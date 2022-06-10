from logging import setLogRecordFactory
import pytest

from jsninjify.models import Descriptive, Buzzword, Word

class TestWord(object):
    def test_init(self):
        w = Word(id = 1, word = "testWord")

        assert w.id == 1
        assert w.word == "testWord"

class TestBuzzword(object):
    def test_init(self):
        bw = Buzzword(id = 1, buzzword = "testBuzzword")

        assert bw.id == 1
        assert bw.buzzword == "testBuzzword"

    def test_get(self):
        descriptive = list(Buzzword
                    .select(Buzzword, Word.word).distinct()
                    .join(Descriptive)
                    .join(Word)
                    .where(Buzzword.buzzword == "buzz").dicts())
        
        supposedWords = ["word", "word1", "word2", "word3", "word4"]

        for i in descriptive:
            assert i["buzzword"] == "buzz2cls"
            assert i["word"] in supposedWords

class TestDescriptive(object):
    def test_init(self):
        d = Descriptive(buzzword_id = 1, word_id = 2)

        assert d.buzzword_id.id == 1
        assert d.word_id.id == 2