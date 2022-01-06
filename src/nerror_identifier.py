from src.span_matcher import SpanMatcher
from src.error_logger import ErrorLogger

class ErrorIdentifier:
    def __init__(self, doc, ground_truth_list, vocab, labels):
        self.doc = doc
        self.vocab = vocab
        self.labels = labels
        predicted = [ent for ent in self.doc.ents if ent.label_ in labels]
        self.predicted_entities = predicted
        matcher = SpanMatcher(self.doc, self.vocab, ground_truth_list, 'GOLD')
        self.ground_truth_entities = matcher.get_span_objects()

    def identify_errors(self) -> None:
        print("\n\n")
        ErrorLogger(self.doc).log_ner_errors(self.ground_truth_entities)
        print('\n\n')

