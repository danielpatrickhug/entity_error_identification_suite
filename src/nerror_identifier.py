import pandas as pd
import numpy as np
import re
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
        self.ground_truth_entities = self.create_entity_span_objects(self.ground_truth_list)


    def add_ground_truth_to_doc(self, ground_truth_spans):
            for idx, ent in enumerate(ground_truth_spans):
                for doc_ent in self.doc.ents:
                    if doc_ent.start == ent.start and doc_ent.end == ent.end:
                        #print(f'Ground Truth: {ent} already in doc')
                        break_loop = True
                        break
                    elif doc_ent.start == ent.start-1 and doc_ent.end == ent.end:
                        print(f"Prediction: {self.doc[doc_ent.start:doc_ent.end]} {doc_ent.start} {doc_ent.end}- is a concatenation of ground truth - {self.doc[ent.start:ent.end]}  {ent.start} {ent.end}")
                        break_loop = True
                        break
                    elif doc_ent.start == ent.start and doc_ent.end == ent.end+1:
                        print(f"Prediction: {self.doc[doc_ent.start:doc_ent.end]} {doc_ent.start} {doc_ent.end}- is a concatenation of ground truth - {self.doc[ent.start:ent.end]} {ent.start} {ent.end}")
                        break_loop = True
                        break
                    elif doc_ent.start == ent.start-1 and doc_ent.end == ent.end+1:
                        print(f"Prediction: {self.doc[doc_ent.start:doc_ent.end]} {doc_ent.start} {doc_ent.end} - is a concatenation of ground truth - {self.doc[ent.start:ent.end]}  {ent.start} {ent.end}")
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
                        print("Unhandled exception: ", ent.text, ent.start, ent.end)


    '''
    input: list of ground truth entity strings
    output: list of span objects for the ground truth entities in self.doc
    '''
    def create_entity_span_objects(self, ground_truth_list):
        return self.match_entity_span_objects(ground_truth_list)

    def match_entity_span_objects(self,entities):
        for idx, ent in enumerate(entities):
            self.match_entity_pattern(idx, ent)
        matches = self.matcher(self.doc)
        return self.create_spans_for_matches(matches)

    def match_entity_pattern(self, idx, ent):
        char_tuple = [(",", " , "), ("-", " - "), ("'", " '"), (".", " . ")]
        for char in char_tuple:
            ent = ent.replace(char[0], char[1])
        tok_patterns = []
        for tok in ent.split():
            tok_patterns.append({'TEXT': tok})
        self.matcher.add(f"ENTITY_{idx}", [tok_patterns])

    def create_spans_for_matches(self, matches):
        spans = []
        for _, start, end in matches:
            span_obj = Span(self.doc, start, end, label="GOLD")
            spans.append(span_obj)
        return spans


    def identify_errors(self):
        self.add_ground_truth_to_doc(self.ground_truth_entities)
        print('_____________________\n')
