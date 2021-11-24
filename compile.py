#!/usr/bin/env python3

import os
import json
from jinja2 import Environment, FileSystemLoader


GENERATED_PATH = './generated'


def load_templates_env(pathname):
    file_loader = FileSystemLoader(pathname)
    return Environment(loader=file_loader)


def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def render_libraries(libraries, indent):
    return ' \\\n{}'.format(indent).join(libraries)


def render_dockerfile(os_name, config, templates_env):
    cfg = config[os_name]
    dockerfile = templates_env.get_template(f'{os_name}.Dockerfile')
    for os_version in cfg['versions']:
        for compiler in cfg['compilers']:
            for compiler_version in cfg['compiler_versions']:
                output = dockerfile.render(
                    os_version=os_version,
                    cc=compiler['cc'],
                    cxx=compiler['cxx'],
                    compiler_version=compiler_version,
                    libraries_to_install=render_libraries(cfg['libraries'], ' ' * 6)
                )
                with open('{}/{}-{}-{}-{}.Dockerfile'.format(
                    GENERATED_PATH, os_name, os_version, compiler['cc'], compiler_version
                ), 'w') as file:
                    file.write(f'{output}\n')


def main():
    if not os.path.isdir(GENERATED_PATH):
        os.makedirs(GENERATED_PATH)

    env = load_templates_env('./templates')
    config = load_config('./config.json')

    render_dockerfile('alpine', config, env)
    render_dockerfile('ubuntu', config, env)


if __name__ == '__main__':
    main()
