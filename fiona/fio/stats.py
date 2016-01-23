from collections import defaultdict

import click
from cligj import features_in_arg


@click.command(short_help="summary statistics")
@features_in_arg
@click.pass_context
def stats(ctx, features):
    attr_names = set()
    values = defaultdict(list)
    for feature in features:
        prop = feature['properties']
        for key, value in prop.items():
            attr_names.add(key)
            values[key].append(value)

    print "attr n min max sum"
    for attr, values in values.items():
        try:
            total = sum(values)
        except TypeError:
            total = "--"

        row = (
            attr,
            len(values),
            min(values),
            max(values),
            total)
        print "{} \t {} \t {} \t {} \t {}".format(*row)
