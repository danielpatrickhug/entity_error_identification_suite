# Entity Error Identification Suite

- This is a Module for detecting concatenation errors for spacy pipeline NER predictions given gold standard entities.
- Module based of NERror: https://github.com/HindsightTechnologySolutions/NERror
- Currently this solution is a bit hacky and only detects concatenation errors.
- TODO:
    - add fragmentation error detections.
    - add disambiguation error detections.
    - add an error logger to file

```bash
python3.9 -m venv venv && source venv/bin/activate && pip install -U pip setuptools wheel
pip install -r requirements.txt
cd src
python main.py
```