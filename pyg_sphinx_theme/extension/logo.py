from docutils import nodes


def logo_role(name, rawtext, text, *args, **kwargs):
    node = nodes.inline(text=text)
    node.set_class('inline-logo')
    node.set_class(name)
    return [node], []
