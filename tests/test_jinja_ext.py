#!/usr/bin/env python
import os
from jinja2 import Environment, FileSystemLoader
from jinja_datatables.jinja_extensions.datatableext import DatatableExt
from jinja_datatables.datatable_classes import DatatableColumn, DatatableTable


def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_dir = os.path.join(current_dir, "./templates")
    env = Environment(loader=FileSystemLoader(template_dir), extensions=[DatatableExt])
    template = env.get_template("datatable_template.html")

    columns = [
        DatatableColumn("data_name", "Column Name", "filter_text"),
    ]
    endpoint = "/get_data"
    rpp = 25
    processing = True
    selector = ".myDataTable"
    table_view = DatatableTable(
        columns,
        endpoint,
        rpp,
        processing,
        selector,
    )
    print(template.render(
        table_view=table_view
    ))


if __name__ == '__main__':
    main()
