from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html'])
)

def render(template, **options):
    tmpl = env.get_template(template)
    options = options or {}
    return tmpl.render(**options)
