#!/usr/bin/env python3

import os
import json
import argparse
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
                with open('{}/{}-{}.Dockerfile'.format(GENERATED_PATH, os_name, compiler['cc']), 'w') as file:
                    file.write(f'{output}\n')


def render_single_dockerfile(os_name, os_version, cc, compiler_version, config, templates_env):
    cfg = config[os_name]
    dockerfile = templates_env.get_template(f'{os_name}.Dockerfile')
    output = dockerfile.render(
        os_version=os_version,
        cc=cc,
        compiler_version=compiler_version,
        libraries_to_install=render_libraries(cfg['libraries'], ' ' * 6)
    )
    with open('Dockerfile', 'w') as file:
        file.write(f'{output}\n')


def main(**kwargs):
    env = load_templates_env('./templates')
    config = load_config('./config.json')

    if all(kwargs.values()):
        render_single_dockerfile(
            os_name=kwargs['os_name'],
            os_version=kwargs['os_version'],
            cc=kwargs['cc'],
            compiler_version=kwargs['cc_version'],
            config=config,
            templates_env=env
        )
    else:
        if not os.path.isdir(GENERATED_PATH):
            os.makedirs(GENERATED_PATH)

        render_dockerfile('alpine', config, env)
        render_dockerfile('ubuntu', config, env)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-on", "--os-name", required=False, help="os")
    ap.add_argument("-ov", "--os-version", required=False, help="os version")
    ap.add_argument("-c", "--cc", required=False, help="compiler")
    ap.add_argument("-cv", "--cc-version", required=False, help="compiler version")
    args = vars(ap.parse_args())

    main(**args)
