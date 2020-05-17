#!/usr/bin/env python
import os
from jinja2 import Environment, FileSystemLoader
from jinja_datatables.jinja_extensions.datatableext import DatatableExt
from jinja_datatables.datatable_classes import DatatableColumn, AjaxDatatable, JSArrayDatatable, HTMLDatatable


def test_ajax(template):
    columns = [
        DatatableColumn("data_name", "Column Name", "filter_text"),
    ]
    endpoint = "/get_data"
    table_view = AjaxDatatable(
        columns,
        None,
        None,
        endpoint,
    )
    return template.render(table_view=table_view)


def test_js_array(template):
    columns = [
        DatatableColumn("data_name", "Column Name", "text"),
    ]
    js_array = "dataArray"
    table_view = JSArrayDatatable(
        columns,
        None,
        None,
        js_array,
    )
    return template.render(table_view=table_view)


def test_html(template):
    columns = [
        DatatableColumn("data_name", "Column Name", "filter_text"),
    ]
    table_view = HTMLDatatable(
        columns,
        None,
        None,
    )
    return template.render(table_view=table_view)


def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    template_dir = os.path.join(current_dir, "./templates")
    env = Environment(loader=FileSystemLoader(template_dir), extensions=[DatatableExt])
    template = env.get_template("datatable_template.html")

    print(test_ajax(template))
    # print(test_js_array(template))
    # print(test_html(template))


if __name__ == '__main__':
    main()
