from __future__ import print_function
from collections import defaultdict

import click
from tabulate import tabulate
from cligj import features_in_arg


@click.command(short_help="summary statistics")
@features_in_arg
@click.option("--unique", default=None)
@click.pass_context
def stats(ctx, features, unique):
    attr_names = set()
    values = defaultdict(list)
    for feature in features:
        prop = feature['properties']
        for key, value in prop.items():
            attr_names.add(key)
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass

            values[key].append(value)

    if unique:
        for val in set(values[unique]):
            click.echo(val)
    else:
        headers = "attr min mean max n".split()
        rows = []
        for attr, values in values.items():
            n = len(values)
            try:
                total = sum(values)
                mean = total / float(n)
            except TypeError:
                total = ""
                mean = ""

            row = (
                attr,
                min(values),
                mean,
                max(values),
                n)
            rows.append(row)

        print(tabulate(rows, headers=headers))
