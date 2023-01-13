from pyg_sphinx_theme.extension.slack import SlackButton


def setup(app):
    app.add_directive('slack', SlackButton)
    app.add_js_file('js/onload.js')

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
