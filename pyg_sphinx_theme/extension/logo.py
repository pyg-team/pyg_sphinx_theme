from docutils import nodes


def logo_role(name, rawtext, text, *args, **kwargs):
    node = nodes.inline(text=text if text != 'null' else '')
    node['classes'] += ['inline-logo', name]
    return [node], []
