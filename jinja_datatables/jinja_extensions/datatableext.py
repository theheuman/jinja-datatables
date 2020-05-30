import os
from jinja2 import lexer, nodes, Environment, FileSystemLoader, Markup
from jinja2.ext import Extension


class DatatableExt(Extension):
    tags = set(['datatable'])

    def _datatable(self, table_view):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        template_dir = os.path.join(current_dir, "../static_assets")
        env = Environment(loader=FileSystemLoader(template_dir))
        template_name = "html/" + table_view.datatable_type.value
        template = env.get_template(template_name)

        html = Markup(template.render(table_view=table_view))
        return html

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [parser.parse_expression()]

        call = self.call_method('_datatable', args, lineno=lineno)
        token = parser.stream.current
        if token.test('name:as'):
            next(parser.stream)
            as_var = parser.stream.expect(lexer.TOKEN_NAME)
            as_var = nodes.Name(as_var.value, 'store', lineno=as_var.lineno)
            return nodes.Assign(as_var, call, lineno=lineno)
        else:
            return nodes.Output([call], lineno=lineno)
