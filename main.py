from src.spacy_pipeline_config import PipelineConfig
from src.data_preprocessor import DataPreProcessor
from src.nerror_identifier import ErrorIdentifier

config = PipelineConfig("en_core_web_trf")
nlp = config.get_nlp()
vocab = config.get_voab()
processor = DataPreProcessor("./data/test.json", "index")
df = processor.get_dataframe()
labels = ["PERSON", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART"]
#stop_words = config.get_stop_words()
#conj_advs = config.get_conj_advs()

for index, row in df.iterrows():
    doc = nlp(row["text"])
    ground_truth_list = list(row["ground_truth_entities_list"])
    id = index
    error_identifier = ErrorIdentifier(id, doc, ground_truth_list, vocab, labels)
    error_identifier.identify_errors()

