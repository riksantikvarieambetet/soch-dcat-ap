# SOCH DCAT-AP

Script for generating a single DCAT-AP RDF from SOCH it self.

![SOCH DCAT-AP](https://github.com/riksantikvarieambetet/soch-dcat-ap/actions/workflows/soch-dcat-ap.yml/badge.svg?branch=master)

## Setup

**Prerequisites**

 - Python 3
 - [Pipenv](https://docs.pipenv.org/)

Cloning:

```
git clone https://github.com/riksantikvarieambetet/soch-dcat-ap.git
```

Installing dependencies and running:
```
pipenv install
pipenv run python3 source/index.py
```

The generated RDF should be created within the output directory.
