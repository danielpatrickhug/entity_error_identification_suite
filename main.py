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

df.apply(lambda x: ErrorIdentifier(nlp(x["text"]), list(x["ground_truth_entities_list"]), vocab, labels).identify_errors(), axis=1)
