#! usr/bin/env python3
import hexlet.fs as fs


def generate():
    tree = fs.mkdir('python-package', [
        fs.mkfile('Makefile'),
        fs.mkfile('README.md'),
        fs.mkdir('dist', [], {}),
        fs.mkdir('tests', [fs.mkfile('test_solution.py')]),
        fs.mkfile('pyproject.toml'),
        fs.mkdir('.venv', [
            fs.mkdir('lib', [
                fs.mkdir('python3.6', [
                    fs.mkdir('site-packages', [
                        fs.mkfile('hexlet-python-packages.egg-link')
                    ])
                ])
            ])
        ], {'owner': 'root', 'hidden': False})
    ], {'hidden': True})

    return tree


print(generate())
