"""
A simple script to validate YAML specifications against their agreed schem
"""

import argparse
import os
import yaml
import simplejson as json
from jsonschema import validate, ValidationError

SCHEMA_DIR = os.path.join(os.path.dirname(__file__), '../schemas')
DEFAULT_SCHEMA = os.path.join(SCHEMA_DIR, 'performance-report.json')


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-s', '--schema', default=DEFAULT_SCHEMA, help='the schema to use for validation (default {}'.format(DEFAULT_SCHEMA))
    parser.add_argument('specification', help='the YAML specification to validate')
    return parser.parse_args()


def main():
    args = parse_args()
    with open(args.schema) as sp:
        schema = json.load(sp)
    with open(args.specification) as fp:
        spec = yaml.load(fp)
    try:
        validate(spec, schema)
        print('{} validates against {}'.format(os.path.basename(args.specification), os.path.basename(args.schema), ))
    except ValidationError as e:
        print('{} failed to validate against {}: {}'.format(os.path.basename(args.specification), os.path.basename(args.schema), e.message, ))


if __name__ == '__main__':
    main()
