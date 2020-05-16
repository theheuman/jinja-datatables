from typing import List


class DatatableColumn:
    data_name: str
    column_name: str
    filter_type: str

    def __init__(self, data_name: str, column_name: str, filter_type: str):
        self.data_name = data_name
        self.column_name = column_name
        self.filter_type = filter_type


class DatatableTable:
    columns: List[DatatableColumn]  # the columns you want shown
    endpoint: str  # the endpoint from where data is populated
    records_per_page: int  # the amount of records per page by default
    processing: bool  # whether datatable shows processing screen or not
    datatable_selector: str  # html selector for the datatable you want populated

    def __init__(
            self, columns, endpoint, records_per_page, processing, datatable_selector
    ):
        self.columns = columns
        self.endpoint = endpoint
        self.records_per_page = records_per_page
        self.processing = processing
        self.datatable_selector = datatable_selector
        self.columns_dict = {
            col.data_name: {
                "column_name": col.column_name,
                "filter_type": col.filter_type,
            }
            for col in self.columns
        }
        self.processing_as_string = str(self.processing).lower()
