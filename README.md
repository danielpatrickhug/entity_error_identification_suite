# Entity NERror Identification Suite

- This is a Module for detecting concatenation, fragmentation and disambiguation errors for spacy pipeline NER predictions given gold standard entities.
- Module based off NERror: https://github.com/HindsightTechnologySolutions/NERror
- Use en_core_web_md to see frag errors for test data
- Opensource TODO:
    - add disambiguation error detection and logging.
    - add spacy-transformers
    - UI to visualize text and to hand label entities by highlighting. higlighted entities get passed to ErrorIdentifier. javascript
    - add Spacy retraining project config library https://explosion.ai/blog/spacy-v3-project-config-systems
    - A nice to have would be a scheduling system for data labeling. i.e Schedule labeling tasks for N number of text articles a day for a given         time period. May allow one person to label a large dataset overtime through consistency. Relabel Queue https://github.com/ankitects/anki 

```bash
python3.9 -m venv venv && source venv/bin/activate && pip install -U pip setuptools wheel
pip install -r requirements.txt
python main.py --model_name en_core_web_trf --data_path ./data/test.json
```
