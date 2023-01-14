from pyg_sphinx_theme.extension.logo import logo_role
from pyg_sphinx_theme.extension.slack import SlackButton


def setup(app):
    app.add_directive('slack', SlackButton)

    app.add_role('pyg', logo_role)
    app.add_role('pytorch', logo_role)

    app.add_js_file('js/on_pyg_load.js')

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
