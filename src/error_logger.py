#from src.logger_utils import add_entity_to_doc

class ErrorLogger:
    def __init__(self, doc):
        self.doc = doc

    def log_concat_error(self, doc_ent, ent) -> None:
        print(f"Concatenation Error\t{self.doc[doc_ent.start:doc_ent.end]}\t{self.doc[ent.start:ent.end]}")

    def log_frag_error(self, doc_ent, ent) -> None:
        print(f"Fragmentation Error\t{self.doc[doc_ent.start:doc_ent.end]}\t{self.doc[ent.start:ent.end]}")

    def log_ner_errors(self, ground_truth_spans: list) -> None:
        break_loop = False
        for idx, ent in enumerate(ground_truth_spans):
            for doc_ent in self.doc.ents:
                if doc_ent.start == ent.start and doc_ent.end == ent.end:
                    #print(f'Ground Truth: {ent} already in doc')
                    break_loop = True
                    break
                elif doc_ent.start == ent.start-1 and doc_ent.end == ent.end:
                    self.log_concat_error(doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start and doc_ent.end == ent.end+1:
                    self.log_concat_error(doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start-1 and doc_ent.end == ent.end+1:
                    self.log_concat_error(doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start and doc_ent.end == ent.end-1 :
                    self.log_frag_error(doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start-1 and doc_ent.end == ent.end-1 and len(doc_ent) != 1:
                    self.log_frag_error(doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start+1 and doc_ent.end == ent.end+1:
                    self.log_frag_error(doc_ent, ent)
                    break_loop = True
                    break
                elif doc_ent.start == ent.start+1 and doc_ent.end == ent.end-1:
                    self.log_frag_error(doc_ent, ent)
                    break_loop = True
                    break
            if break_loop:
                break_loop = False
                continue
            #For debugging purposes
            #else:
                #add_entity_to_doc(self.doc,ent)
