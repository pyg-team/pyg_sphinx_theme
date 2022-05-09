from setuptools import find_packages, setup

__version__ = '0.1.0'

setup(
    name='pyg_sphinx_theme',
    version=__version__,
    author='PyG Team',
    author_email='team@pyg.org',
    url='https://github.com/pyg-team/pyg_sphinx_theme',
    install_requires=[
        'sphinx',
        'sphinx_rtd_theme',
    ],
    package_data={'pyg_sphinx_theme': [
        'theme.conf',
    ]},
    entry_points={
        'sphinx.html_themes': [
            'pyg_sphinx_theme = pyg_sphinx_theme',
        ]
    },
    packages=find_packages(),
    include_package_data=True,
)
