# rulebased-slim-mv


## Abstract

The django sample application to calculate points of a fictious credit card.
We try to avoid the "Fat" model/view problem by embedding the rule engine into our django application.

## Env 

- Python 3.10.12 
- VSCode 1.81.1
- WSL2 (Ubuntu)

## Set up


python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

create `point_calculation/.env` file, and set propertyies as bellow.
```
SECRET_KEY='xxxxxxxxxxxxxxxxxxxx'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

python point_calculation/manage.py loaddata point_calculation/point/fixtures/init_data.json

http://127.0.0.1:8000/point/
