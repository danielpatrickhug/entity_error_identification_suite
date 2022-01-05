import spacy

class PipelineConfig:
    def __init__(self, model_name="en_core_web_trf"):
        self.nlp = spacy.load(model_name)
        self.vocab = self.nlp.vocab

    def get_nlp(self):
        return self.nlp

    def get_voab(self):
        return self.vocab

    def get_stop_words(self):
        with open("./data/stoplist.txt", "r") as a_file:
            for line in a_file:
                self.stop_words = []
                self.stop_words.append(line)
        return self.stop_words

    def get_conj_advs(self):
        with open("./data/conj_advs.txt", "r") as a_file:
            for line in a_file:
                self.conj_advs = []
                self.conj_advs.append(line)
        return self.conj_advs