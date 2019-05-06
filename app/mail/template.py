from jinja2 import Environment, PackageLoader, select_autoescape


class Template(object):
    def __init__(self):
        self.templateEnv = Environment(loader=PackageLoader('app.mail', 'templates'),
                                              autoescape=select_autoescape(['html', 'xml']))

    def renderEmail(self, info, status):
        template = self.templateEnv.get_template("info.html")
        return template.render(info=info, status=status)
