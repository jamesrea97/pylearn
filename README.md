# Python concurrency Notes

Please refer to `./NOTES.md` for detailed notes.

## Running examples

With each set of notes, there are accompanying sample code found in `./src`.
You can run these as follows:
```py
python ./src/{{name_topic}}.py
```

## Deployment
Python=3.9

### Local
```
virtualenv venv --python=/path/to/python/3.9
source venv/bin/activate
pip install -r ./requirements/prod.txt
python ./src/app.py
```
