from src.span_matcher import SpanMatcher
from src.error_logger import ErrorLogger

class ErrorIdentifier:
    def __init__(self, doc: object, ground_truth_list: list, vocab: object, labels: list) -> None:
        self.doc = doc
        self.doc.ents = [ent for ent in self.doc.ents if ent.label_ in labels]
        matcher = SpanMatcher(self.doc, vocab, ground_truth_list, 'GOLD')
        self.ground_truth_entities = matcher.get_span_objects()

    def identify_errors(self) -> None:
        print("\n\n")
        ErrorLogger(self.doc).log_ner_errors(self.ground_truth_entities)
        print('\n\n')

