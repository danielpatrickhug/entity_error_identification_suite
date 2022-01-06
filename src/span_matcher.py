from spacy.tokens import Span
from spacy.matcher import Matcher

class SpanMatcher:
    def __init__(self, doc: object, vocab: object, entity_list: list, label: str) -> None:
        self.doc = doc
        self.vocab = vocab
        self.matcher = Matcher(self.vocab)
        self.entity_list = entity_list
        self.label = label
        for idx, ent in enumerate(self.entity_list): self.match_string_to_doc_obj(idx, ent)
        self.matches = self.matcher(self.doc)

    def match_string_to_doc_obj(self, idx: int, ent: str) -> None:
        char_tuple_list = [(",", " , "), ("-", " - "), ("'", " '"), (".", " . ")]
        for char_tuple in char_tuple_list: ent = ent.replace(char_tuple[0], char_tuple[1])
        tok_patterns = [{'TEXT': tok} for tok in ent.split()]
        self.matcher.add(f"ENTITY_{idx}", [tok_patterns])

    def get_span_objects(self) -> list:
        return [Span(self.doc, start, end, label=self.label) for _, start, end in self.matches]