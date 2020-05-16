#!/usr/bin/env python
from jinja2 import Environment
from jinja_datatables.jinja_extensions.datatableext import DatatableExt


def main():
    template = Environment(extensions=[DatatableExt]).from_string('{% datatable "example" %}')
    print(template.render())


if __name__ == '__main__':
    main()
