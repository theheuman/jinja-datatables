from flask import Flask,  jsonify
from flask.templating import render_template
from jinja_datatables.datatable_classes import DatatableColumn, AjaxDatatable
from jinja_datatables.jinja_extensions.datatableext import DatatableExt

from data import DATA

app = Flask(__name__)  # , instance_relative_config=True)
app.jinja_options["extensions"].append(DatatableExt)


@app.route("/")
def index():
    columns = [
        DatatableColumn("name", "Club Name", "text"),
        DatatableColumn("location", "City", "select"),
        DatatableColumn("dateFounded", "Founded", "date")
    ]
    html_arguments = {"id": "premier-league-teams-table", "class": "table", "style": "width: 60%;"}
    datatable_arguments = {"processing": "true"}
    table_view = AjaxDatatable(columns, html_arguments, datatable_arguments, "/get_data")
    return render_template("index.html", title="Premier League Teams", table_view=table_view)


@app.route("/get_data")
def get_data():
    response = dict(data=DATA)
    print(response)
    return jsonify(response)


if __name__ == "__main__":
    app.run()