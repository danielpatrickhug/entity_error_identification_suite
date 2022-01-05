from spacy.tokens import Span
from spacy.matcher import Matcher

class ErrorIdentifier:
    def __init__(self, text_id, doc, ground_truth_list, vocab, labels):
        self.doc = doc
        self.vocab = vocab
        self.text_id = text_id
        self.matcher = Matcher(self.vocab)
        self.labels = labels
        self.ground_truth_list = ground_truth_list
        self.predicted_entities = [ent for ent in self.doc.ents if ent.label_ in labels]
        [self.match_string_to_doc_obj(idx, ent) for idx, ent in enumerate(self.ground_truth_list)]
        self.matches = self.matcher(self.doc)
        self.ground_truth_entities = self.create_gs_spans_for_matches()

    def match_string_to_doc_obj(self, idx: int, ent: str):
        char_tuple = [(",", " , "), ("-", " - "), ("'", " '"), (".", " . ")]
        for char in char_tuple:
            ent = ent.replace(char[0], char[1])
        tok_patterns = []
        for tok in ent.split():
            tok_patterns.append({'TEXT': tok})
        self.matcher.add(f"ENTITY_{idx}", [tok_patterns])

    def create_gs_spans_for_matches(self):
        spans = []
        for _, start, end in self.matches:
            span_obj = Span(self.doc, start, end, label="GOLD")
            spans.append(span_obj)
        return spans

    def log_concat_error(self, doc_ent, ent):
        print(f"Concatenation Error: {self.doc[doc_ent.start:doc_ent.end]} - {self.doc[ent.start:ent.end]}")

    def log_frag_error(self, doc_ent, ent):
        print(f"Fragmentation Error: {self.doc[doc_ent.start:doc_ent.end]} - {self.doc[ent.start:ent.end]}")

    def add_ground_truth_to_doc(self, ground_truth_spans: list):
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
            else:
                try:
                    self.doc.ents = list(self.doc.ents)+[ent]
                except Exception as e:
                    #Look for colliding entities
                    #print(f"Unhandled exception: {doc_ent.text} - {ent.text}")
                    pass

    def identify_errors(self):
        self.add_ground_truth_to_doc(self.ground_truth_entities)
        print('_____________________\n')
