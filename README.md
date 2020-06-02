# Jinja-Datatables

A python library to simplify rendering datatables in jinja templates

**Note**: This tool is in development and doesnt 100% work yet, all of it is untested

## TODO
 - Write test for html
 - Add detail row functionality
 - Make filters an option
 
## Install
 
    pip install jinja-datatables

## Usage
**See this repo's tests folder for an example**
Currently only flask-ajax completed

### 1.) Create a table view object

There are currently three options

#### From Ajax
**Check examples/flask-ajax for a simple example**

If you want to get all your data asynchronously from a endpoint you can create a datatable object like this

    from jinja_datatables.datatable_classes import DatatableColumn, AjaxDatatable
    columns = [
        DatatableColumn("data_name", "Column Name", "text"
    ]
    endpoint = "/get_data"
    table_view = AjaxDatatable(
        columns,
        None,
        None,
        endpoint,
    )

#### From a JS array
**Check my [HOMM3Guide](https://github.com/theheuman/HOMM3Guide/blob/master/build_table.py) for an example**

If you have all your data defined in a JS array you can create a datatable object like this:

    from jinja_datatables.datatable_classes import DatatableColumn, JSArrayDatatable
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

For your endpoint, make sure it returns just an array of your data, functionality to customize this behavior might be added in future

#### From HTML
**This is completely untested**

If you already have your table in html, then you can easily instantiate a datatable on it like this:

    from jinja_datatables.datatable_classes import DatatableColumn, HTMLDatatable
    columns = [
        DatatableColumn("data_name", "Column Name", "text"),
    ]
    table_view = HTMLDatatable(
        columns,
        None,
        None,
    )

### 2.) Instantiate Jinja environment

    from jinja2 import Environment
    from jinja_datatables.jinja_extensions.datatableext import DatatableExt
    env = Environment(extensions=[DatatableExt])

For flask this will be handled by attaching an extension like this:

    app = Flask(__name__)  # , instance_relative_config=True)
    app.jinja_options["extensions"].append(DatatableExt)

### 3.) Render Template

**In python**

    template = env.get_template("datatable_template.html")
    template.render(table_view=table_view)
    
**In your template file**

    {% datatable table_view %}

## Contributing
I have no idea how contributing works. Make a pull request? Send me a message? 

I would greatly appreciate help on how to test this
