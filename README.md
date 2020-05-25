# Jinja-Datatables

A python library to simplify rendering datatables in jinja templates

**Note**: This tool is in development and doesnt 100% work yet, all of it is untested

## TODO
 - Test from ajax in kalhufvudet
 - Write test for html
 - upload to pip for pip install
 - Add detail row functionality
 - Add no filter option (basically make the cell blank)
 - Make filters an option
 
## Usage
**See this repo's tests folder for an example**

Download this repository into your project (hopefully pip install coming soon)


### 1.) Create a table view object

There are currently three options

#### From Ajax
If you want to get all your data asynchronously from a endpoint you can create a datatable oject like this

    from jinja_datatables.datatable_classes import DatatableColumn, AjaxDatatable
    columns = [
        DatatableColumn("data_name", "Column Name", "filter_text"
    ]
    endpoint = "/get_data"
    table_view = AjaxDatatable(
        columns,
        None,
        None,
        endpoint,
    )

#### From a JS array
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


#### From HTML
If you already have your table in html, then you can easily instantiate a datatable on it like this:

    from jinja_datatables.datatable_classes import DatatableColumn, HTMLDatatable
    columns = [
        DatatableColumn("data_name", "Column Name", "filter_text"),
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
