from spacy.tokens import Span
from spacy.matcher import Matcher

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