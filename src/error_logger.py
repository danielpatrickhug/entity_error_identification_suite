from spacy.tokens.span import Span


class ErrorLogger:
    def __init__(self, doc: object) -> None:
        self.doc = doc
        # Tuple: (error_label, start_offset, end_offset, check_singleton_flag)
        self.error_types = [("Correct Entity Prediction", 0, 0, 0),("Start Concatenation Error", -1, 0, 0), ("End Concatenation Error", 0, 1, 0),
                       ("Bilateral Concatenation Error", -1, 1, 0), ("Shift Left Fragmentation Error", -1, -1, 1), ("End Fragmentation Error", 0, -1, 0),
                        ("Shift Right Fragmentation Error", 1, 1, 1), ("Bilateral Fragmentation Error", 1, -1, 1), ("Start Fragmentation Error", 1, 0, 0)
                        , ("Start Fragmentation Error", 2, 0, 0)]

    #TODO Log to tsv
    def log_general(self, prediction_type: str, doc_ent: Span, ent: Span) -> None:
        print(f"{prediction_type} \t {self.doc[doc_ent.start:doc_ent.end]} \t {self.doc[ent.start:ent.end]}")

    def is_not_singleton(self, ent: Span) -> bool:
        return len(ent) != 1

    def check_entity_pair(self, doc_ent: Span, ent: Span, error_tuple) -> bool:
        if error_tuple[3] == 1:
            if doc_ent.start == ent.start+error_tuple[1] and doc_ent.end == ent.end+error_tuple[2] and self.is_not_singleton(doc_ent):
                self.log_general(error_tuple[0], doc_ent, ent)
                return True
        else:
            if doc_ent.start == ent.start+error_tuple[1] and doc_ent.end == ent.end+error_tuple[2]:
                self.log_general(error_tuple[0], doc_ent, ent)
                return True

    def get_overlapping_entities(self, ent: Span) -> list:
        return [doc_ent for doc_ent in self.doc.ents if doc_ent.end>= ent.start and doc_ent.start<= ent.end]

    #TODO break into separate classes(FragmentError, ConcatenationError)
    #TODO add DisambiguationError logger and create error class
    def log_ner_errors(self, ground_truth_spans: list) -> None:
        for idx, ent in enumerate(ground_truth_spans):
            for doc_ent in self.get_overlapping_entities(ent):
                for error_type in self.error_types:
                    if self.check_entity_pair(doc_ent, ent, error_type):
                        break



