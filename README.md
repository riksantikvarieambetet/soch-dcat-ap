# SOCH DCAT AP

Script for generating a single DCAT-AP RDF from SOCH it self.

## Setup

**Prerequisites**

 - Python 3
 - [Pipenv](https://docs.pipenv.org/)

Cloning:

```
git clone https://github.com/riksantikvarieambetet/soch-dcat-ap.git
```

You should rename `config.ini.example` to `config.ini` and replace the value `test` with your SOCH API key.

Installing dependencies and running:
```
pipenv install
pipenv run python3 source/index.py
```

The generated RDF should be created within the output directory.
