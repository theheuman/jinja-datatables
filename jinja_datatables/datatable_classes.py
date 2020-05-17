from typing import List
from enum import Enum

class DatatableColumn:
    data_name: str
    column_name: str
    filter_type: str

    def __init__(self, data_name: str, column_name: str, filter_type: str):
        self.data_name = data_name
        self.column_name = column_name
        self.filter_type = filter_type


class DatatableType(Enum):
    AJAX = "from_ajax.html"
    JS_ARRAY = "from_js_array.html"
    HTML = "from_html.html"


class DatatableTable:
    columns: List[DatatableColumn]  # the columns you want shown
    html_arguments: dict # key value pairs to be set on the table element, if it does not contain id, it will be assigned as "example"
    html_default_arguments = {
        "id": "example",
        "class": "table",
    }
    datatable_arguments: dict # key value pairs to be plugged in to the datatables constructor
    datatable_default_arguments = {
        "records_per_page": 25,
        "processing": "true",
    }
    datatable_type: DatatableType

    def __init__(
            self, columns, html_arguments, datatable_arguments, datatable_type,
    ):
        self.columns = columns

        for key, value in self.html_default_arguments.items():
            if key not in html_arguments:
                html_arguments[key] = value
        self.html_arguments = html_arguments

        for key, value in self.datatable_default_arguments.items():
            if key not in datatable_arguments:
                datatable_arguments[key] = value
        self.datatable_arguments = datatable_arguments

        self.datatable_type = datatable_type

        self.columns_dict = {
            col.data_name: {
                "column_name": col.column_name,
                "filter_type": col.filter_type,
            }
            for col in self.columns
        }


class AjaxDatatable(DatatableTable):
    def __init__(self, columns, html_arguments, datatable_arguments, endpoint):
        super().__init__(columns, html_arguments, datatable_arguments, DatatableType.AJAX)
        self.endpoint = endpoint


class JSArrayDatatable(DatatableTable):
    def __init__(self, columns, html_arguments, datatable_arguments, js_array_variable_name):
        super().__init__(columns, html_arguments, datatable_arguments, DatatableType.JS_ARRAY)
        self.js_array_variable_name = js_array_variable_name


class HTMLDatatable(DatatableTable):
    def __init__(self, columns, html_arguments, datatable_arguments):
        super().__init__(columns, html_arguments, datatable_arguments, DatatableType.HTML)
