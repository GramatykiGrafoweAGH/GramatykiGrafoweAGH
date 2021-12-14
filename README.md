# GramatykiGrafoweAGH

Gramatyka grafowa do rekurencyjnej adaptacji siatek czworokątnych

### Setup

```
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
(.venv) $ pip install -e .
```

### Lint

```
(.venv) $ pip install flake8
(.venv) $ flake8 . --ignore E501,E741 --exclude .venv,build
```

### Test

```
(.venv) $ pip install pytest
(.venv) $ python3 -m pytest
```

### Run

```
(.venv) $ python3 examples/example.py
```
