Verify Data Schemas
===================
YAML specifications for Verify data.
This includes performance reports, events and other data sources.

Getting started
---------------

You can view YAML specifications under `specifications/`

Specifications are not validated automatically. To validate a specification, run:

```bash
python3 -m venv <path to new virtual environment>
source <path to new virtual environment>/bin/activate
pip3 install -r requirements.txt
python3 scripts/validate.py specifications/performance-reports/test.yaml
```

To validate against a given schema

```bash
python3 scripts/validate.py -s schemas/performance-report.json specifications/performance-reports/test.yaml
```

For help


```
python3 scripts/validate.py -h
```

Schemas for specifications are kept under `schemas/`

