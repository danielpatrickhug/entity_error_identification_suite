# Entity Error Identification Suite

- This is a Module for detecting concatenation and fragmentation errors for spacy pipeline NER predictions given gold standard entities.
- Module based of NERror: https://github.com/HindsightTechnologySolutions/NERror
- Currently this solution is a bit hacky and only detects concatenation, and fragmentation errors.
- Use en_core_web_md to see frag errors
- TODO:
    - add granular concatenation error detection.
    - add granular fragmentation error detection.
    - add disambiguation error detection.
    - add an error logger to file

```bash
python3.9 -m venv venv && source venv/bin/activate && pip install -U pip setuptools wheel
pip install -r requirements.txt
python main.py
```