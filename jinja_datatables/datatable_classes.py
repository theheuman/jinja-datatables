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
    records_per_page: int  # the amount of records per page by default
    processing: bool  # whether datatable shows processing screen or not
    datatable_selector: str  # html selector for the datatable you want populated
    extra_datatable_arguments: dict
    type: DatatableType

    def __init__(
            self, columns, records_per_page, processing, datatable_selector, extra_datatable_arguments, type,
    ):
        self.columns = columns
        self.records_per_page = records_per_page
        self.processing = processing
        self.datatable_selector = datatable_selector
        self.extra_datatable_arguments = extra_datatable_arguments
        self.processing_as_string = str(self.processing).lower()
        self.type = type
        self.columns_dict = {
            col.data_name: {
                "column_name": col.column_name,
                "filter_type": col.filter_type,
            }
            for col in self.columns
        }


class AjaxDatatable(DatatableTable):
    def __init__(self, columns, records_per_page, processing, datatable_selector, extra_datatable_arguments, endpoint):
        super(columns, records_per_page, processing, datatable_selector, extra_datatable_arguments, DatatableType.AJAX)
        self.endpoint = endpoint


class JSArrayDatatable(DatatableTable):
    def __init__(self, columns, records_per_page, processing, datatable_selector, extra_datatable_arguments, js_array_variable_name)
        super(columns, records_per_page, processing, datatable_selector, extra_datatable_arguments, DatatableType.JS_ARRAY)
        self.js_array_variable_name = js_array_variable_name


class HTMLDatatable(DatatableTable):
    def __init__(self, columns, records_per_page, processing, datatable_selector, extra_datatable_arguments)
        super(columns, records_per_page, processing, datatable_selector, extra_datatable_arguments, DatatableType.HTML)
