from spacy.tokens.span import Span


class ErrorLogger:
    def __init__(self, doc: object) -> None:
        self.doc = doc
        self.error_types= [
            {
            "Error Name": "Correct Entity Prediction",
            "Start Offset": 0,
            "End Offset": 0,
            "Singleton Flag": 0
            },
            {
            "Error Name": "Start Concatenation Error",
            "Start Offset": -1,
            "End Offset": 0,
            "Singleton Flag": 0
            },
            {
            "Error Name": "End Concatenation Error",
            "Start Offset": 0,
            "End Offset": 1,
            "Singleton Flag": 0
            },
            {
            "Error Name": "Bilateral Concatenation Error",
            "Start Offset": -1,
            "End Offset": 1,
            "Singleton Flag": 0
            },
            {
            "Error Name": "Shift Left Fragmentation Error",
            "Start Offset": -1,
            "End Offset": -1,
            "Singleton Flag": 1
            },
            {
            "Error Name": "End Fragmentation Error",
            "Start Offset": 0,
            "End Offset": -1,
            "Singleton Flag": 1
            },
            {
            "Error Name": "Shift Right Fragmentation Error",
            "Start Offset": 1,
            "End Offset": 1,
            "Singleton Flag": 1
            },
            {
            "Error Name": "Bilateral Fragmentation Error",
            "Start Offset": 1,
            "End Offset": -1,
            "Singleton Flag": 1
            },
            {
            "Error Name": "Start Fragmentation Error",
            "Start Offset": 1,
            "End Offset": 0,
            "Singleton Flag": 1
            },
            {
            "Error Name": "Start Fragmentation Error",
            "Start Offset": 2,
            "End Offset": 0,
            "Singleton Flag": 1
            }]

    #TODO Log to tsv
    def log_general(self, prediction_type: str, doc_ent: Span, ent: Span) -> None:
        print(f"{prediction_type} \t {self.doc[doc_ent.start:doc_ent.end]} \t {self.doc[ent.start:ent.end]}")

    def is_not_singleton(self, ent: Span) -> bool:
        return len(ent) != 1

    def check_entity_pair(self, doc_ent: Span, ent: Span, error_dict) -> bool:
        if error_dict["Singleton Flag"] == 1:
            if doc_ent.start == ent.start+error_dict["Start Offset"] and doc_ent.end == ent.end+error_dict["End Offset"] and self.is_not_singleton(doc_ent):
                self.log_general(error_dict["Error Name"], doc_ent, ent)
                return True
        else:
            if doc_ent.start == ent.start+error_dict["Start Offset"] and doc_ent.end == ent.end+error_dict["End Offset"]:
                self.log_general(error_dict["Error Name"], doc_ent, ent)
                return True

    def get_overlapping_entities(self, ent: Span) -> list:
        return [doc_ent for doc_ent in self.doc.ents if doc_ent.end>= ent.start and doc_ent.start<= ent.end]

    #TODO break into separate classes(FragmentError, ConcatenationError)
    #TODO add DisambiguationError logger and create error class
    def log_ner_errors(self, ground_truth_spans: list) -> None:
        for idx, ent in enumerate(ground_truth_spans):
            for doc_ent in self.get_overlapping_entities(ent):
                for error_type_dict in self.error_types:
                    if self.check_entity_pair(doc_ent, ent, error_type_dict):
                        break



