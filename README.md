# SOCH DCAT AP

Script for generating a single DCAT-AP RDF from SOCH it self.

[![Build Status](https://travis-ci.com/riksantikvarieambetet/soch-dcat-ap.svg?branch=master)](https://travis-ci.com/riksantikvarieambetet/soch-dcat-ap)

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
