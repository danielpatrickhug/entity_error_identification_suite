# Entity NERror Identification Suite

- This is a Module for detecting concatenation, fragmentation and disambiguation errors for spacy pipeline NER predictions given gold standard entities.
- Module based off NERror: https://github.com/HindsightTechnologySolutions/NERror
- Use en_core_web_md to see frag errors for test data
- TODO:
    - add disambiguation error detection and logging.
    - UI to visualize text and to hand label entities by highlighting. higlighted entities get passed to ErrorIdentifier. Prodigy
    - add Spacy retraining project config library https://explosion.ai/blog/spacy-v3-project-config-systems
    - End Goal: Active learning - labeling and retraining pipeline with error logging.
    - I have a cleanup script to generate 'silver' entities on a local branch. Potential Feature.
    - A nice to have would be a scheduling system for data labeling. i.e Schedule labeling tasks for N number of text articles for a given time         period.

```bash
python3.9 -m venv venv && source venv/bin/activate && pip install -U pip setuptools wheel #Use an alias
pip install -r requirements.txt
python main.py --model_name en_core_web_trf --data_path ./data/test.json
```
