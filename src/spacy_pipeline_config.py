import spacy
from spacy.tokens import Span
from spacy.matcher import Matcher

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

class SpanMatcher:
    def __init__(self, doc, vocab, ground_truth_list, label):
        self.doc = doc
        self.vocab = vocab
        self.matcher = Matcher(self.vocab)
        self.ground_truth_list = ground_truth_list
        self.label = label
        for idx, ent in enumerate(self.ground_truth_list): self.match_string_to_doc_obj(idx, ent)
        self.matches = self.matcher(self.doc)

    def match_string_to_doc_obj(self, idx: int, ent: str):
        char_tuple = [(",", " , "), ("-", " - "), ("'", " '"), (".", " . ")]
        for char in char_tuple:
            ent = ent.replace(char[0], char[1])
        tok_patterns = [{'TEXT': tok} for tok in ent.split()]
        self.matcher.add(f"ENTITY_{idx}", [tok_patterns])

    def get_span_objects(self):
        return [Span(self.doc, start, end, label=self.label) for _, start, end in self.matches]