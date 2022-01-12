# Entity NERror Identification Suite

- This is a Module for detecting concatenation, fragmentation and disambiguation errors for spacy pipeline NER predictions given gold standard entities.
- Module based off NERror: https://github.com/HindsightTechnologySolutions/NERror
- Use en_core_web_md to see frag errors for test data



```bash
python3.9 -m venv venv && source venv/bin/activate && pip install -U pip setuptools wheel
pip install -r requirements.txt
python main.py --model_name en_core_web_trf --data_path ./data/test.json
```
