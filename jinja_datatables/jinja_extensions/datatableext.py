from jinja2 import lexer, nodes
from jinja2.ext import Extension


class DatatableExt(Extension):
    tags = set(['datatable'])

    def _datatable(self, id_name="example", class_name="myDataTable"):
        return '<table id="' + id_name + '" class="' + class_name + '"></table>'

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [parser.parse_expression()]
        if parser.stream.skip_if("comma"):
            args.append(parser.parse_expression())

        call = self.call_method('_datatable', args, lineno=lineno)
        token = parser.stream.current
        if token.test('name:as'):
            next(parser.stream)
            as_var = parser.stream.expect(lexer.TOKEN_NAME)
            as_var = nodes.Name(as_var.value, 'store', lineno=as_var.lineno)
            return nodes.Assign(as_var, call, lineno=lineno)
        else:
            return nodes.Output([call], lineno=lineno)
