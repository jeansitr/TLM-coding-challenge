from jsninjify.models import Descriptive, Buzzword, Word

class TestWord(object):
    def test_init(self):
        w = Word(id = 1, word = "testWord")

        assert w.id == 1
        assert w.word == "testWord"

    def test_get(self):
        w = Word.get(Word.id == 1)

        assert w.id == 1
        assert w.word is not None

class TestBuzzword(object):
    def test_init(self):
        bw = Buzzword(id = 1, buzzword = "testBuzzword")

        assert bw.id == 1
        assert bw.buzzword == "testBuzzword"

    def test_get(self):
        bw = Buzzword.get(Buzzword.id == 1)

        assert bw.id == 1
        assert bw.buzzword is not None

class TestDescriptive(object):
    def test_init(self):
        d = Descriptive(buzzword_id = 1, word_id = 2)

        assert d.buzzword_id.id == 1
        assert d.word_id.id == 2

    def test_get(self):
        descriptive = list(Buzzword
                    .select(Buzzword, Word.word)
                    .join(Descriptive)
                    .join(Word)
                    .where(Buzzword.id == 1).dicts())

        for i in descriptive:
            assert i["id"] == 1
            
        assert len(descriptive) >= 3