#from src.logger_utils import add_entity_to_doc

from spacy.tokens.span import Span


class ErrorLogger:
    def __init__(self, doc: object) -> None:
        self.doc = doc

    #TODO Log to tsv
    def log_correct_prediction(self, doc_ent: Span, ent: Span) -> None:
        print(f"Correct Entity Prediction \t {self.doc[doc_ent.start:doc_ent.end]} \t {self.doc[ent.start:ent.end]}")

    def log_concat_error(self, concat_type, doc_ent: Span, ent: Span) -> None:
        print(f"{concat_type} Concatenation Error \t {self.doc[doc_ent.start:doc_ent.end]} \t {self.doc[ent.start:ent.end]}")

    def log_frag_error(self, frag_type, doc_ent: Span, ent: Span) -> None:
        print(f"{frag_type} Fragmentation Error \t {self.doc[doc_ent.start:doc_ent.end]} \t {self.doc[ent.start:ent.end]}")

    #TODO break into separate classes(FragmentError, ConcatenationError)
    #TODO add DisambiguationError logger and create error class
    def log_ner_errors(self, ground_truth_spans: list) -> None:
        break_loop = False
        for idx, ent in enumerate(ground_truth_spans):
            overlapping_spans= [doc_ent for doc_ent in self.doc.ents if doc_ent.end>= ent.start and doc_ent.start<= ent.end]
            for doc_ent in overlapping_spans:
                if doc_ent.start == ent.start and doc_ent.end == ent.end:
                    self.log_correct_prediction(doc_ent, ent) # Lack of symmetry in console is ugly
                    break_loop = True
                    break
                elif doc_ent.start == ent.start-1 and doc_ent.end == ent.end:
                    self.log_concat_error("Start", doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start and doc_ent.end == ent.end+1:
                    self.log_concat_error("End", doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start-1 and doc_ent.end == ent.end+1:
                    self.log_concat_error("Bilateral", doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start and doc_ent.end == ent.end-1 :
                    self.log_frag_error("End", doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start-1 and doc_ent.end == ent.end-1 and len(doc_ent) != 1:
                    self.log_frag_error("Shift Left", doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start+1 and doc_ent.end == ent.end+1:
                    self.log_frag_error("Shift Right", doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start+1 and doc_ent.end == ent.end-1 and len(doc_ent) != 1:
                    self.log_frag_error("Contract", doc_ent, ent)
                    break_loop = True
                    break
            if break_loop:
                break_loop = False
                continue
            #For debugging purposes
            #else:
                #add_entity_to_doc(self.doc,ent)
