from spacy.tokens.span import Span

class ErrorLogger:
    def __init__(self, doc: object) -> None:
        self.doc = doc
        self.prediction_types= [
            {"Name": "Correct Entity Prediction", "Start Offset": 0, "End Offset": 0, "Singleton Flag": 0},
            {"Name": "Start Concatenation Error", "Start Offset": -1, "End Offset": 0, "Singleton Flag": 0},
            {"Name": "End Concatenation Error", "Start Offset": 0, "End Offset": 1, "Singleton Flag": 0},
            {"Name": "Bilateral Concatenation Error", "Start Offset": -1, "End Offset": 1, "Singleton Flag": 0},
            {"Name": "Shift Left Fragmentation Error", "Start Offset": -1, "End Offset": -1, "Singleton Flag": 1},
            {"Name": "End Fragmentation Error", "Start Offset": 0, "End Offset": -1, "Singleton Flag": 0},
            {"Name": "Shift Right Fragmentation Error", "Start Offset": 1, "End Offset": 1, "Singleton Flag": 1},
            {"Name": "Bilateral Fragmentation Error", "Start Offset": 1, "End Offset": -1, "Singleton Flag": 1},
            {"Name": "Start Fragmentation Error", "Start Offset": 1, "End Offset": 0, "Singleton Flag": 0},
            {"Name": "Start Fragmentation Error", "Start Offset": 2, "End Offset": 0, "Singleton Flag": 0}]
        self.error_list = []

    #TODO Log to tsv
    def log_general(self, prediction_type: str, doc_ent: Span, ent: Span) -> None:
        print(f"{prediction_type} \t {self.doc[doc_ent.start:doc_ent.end]} \t {self.doc[ent.start:ent.end]}")

    def log_to_list(self, prediction_type: str, doc_ent: Span, ent: Span) -> str:
        return f"{prediction_type} \t {self.doc[doc_ent.start:doc_ent.end]} \t {self.doc[ent.start:ent.end]}"

    def filter_duplicate_logs(self) -> None:
        for log in set(self.error_list):
            print(log)

    def is_not_singleton(self, ent: Span) -> bool:
        return len(ent) != 1

    def get_overlapping_entities(self, ent: Span) -> list:
        return [doc_ent for doc_ent in self.doc.ents if doc_ent.end>= ent.start and doc_ent.start<= ent.end]

    def check_entity_pair(self, doc_ent: Span, ent: Span, prediction_dict: dict) -> bool:
        if prediction_dict["Singleton Flag"] == 1:
            if doc_ent.start == ent.start+prediction_dict["Start Offset"] and doc_ent.end == ent.end+prediction_dict["End Offset"] and self.is_not_singleton(doc_ent):
                #self.log_general(prediction_dict["Name"], doc_ent, ent)
                self.error_list.append(self.log_to_list(prediction_dict["Name"], doc_ent, ent))
                return True
        else:
            if doc_ent.start == ent.start+prediction_dict["Start Offset"] and doc_ent.end == ent.end+prediction_dict["End Offset"]:
                #self.log_general(prediction_dict["Name"], doc_ent, ent)
                self.error_list.append(self.log_to_list(prediction_dict["Name"], doc_ent, ent))
                return True

    def log_ner_errors(self, ground_truth_spans: list) -> None:
        for idx, ent in enumerate(ground_truth_spans):
            for doc_ent in self.get_overlapping_entities(ent):
                for prediction_type_dict in self.prediction_types:
                    if self.check_entity_pair(doc_ent, ent, prediction_type_dict):
                        break
        self.filter_duplicate_logs() #For debugging purposes only. will add filter for TSV later




