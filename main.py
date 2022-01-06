from src.spacy_pipeline_config import PipelineConfig
from src.data_preprocessor import DataPreProcessor
from src.nerror_identifier import ErrorIdentifier
import argparse

#TODO convert to config parser
parser = argparse.ArgumentParser()
parser.add_argument("--model_name", type=str, default="en_core_web_trf")
parser.add_argument("--data_path", type=str, default="./data/test.json")
args = parser.parse_args()

config = PipelineConfig(args.model_name)
nlp = config.get_nlp()
df = DataPreProcessor(args.data_path, "index").get_dataframe()
labels = ["PERSON", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART"]

df.apply(lambda x: ErrorIdentifier(nlp(x["text"]), list(x["ground_truth_entities_list"]),
                                   config.get_vocab(), labels).identify_errors(), axis=1)
