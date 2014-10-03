#!/usr/bin/env python
# vim:tabstop=4

from fabric.api import *

env.user = ''
env.key_filename = ''
#env.password='ugggghhh!'
env.timeout = 10
env.output_prefix = False
env.warn_only = True
#env.abort_on_prompts = True

env.roledefs = {
    'public': [
        '',
        ''
    ],
    'internal1': [
        '',
        ''
    ]
}

def version():
    try:
        run('echo "$(echo "$SSH_CONNECTION" | cut -d" " -f3), $(hostname), $(bash --version | head -n1)"')
    except:
        print('Could not connect and/or run version on this host.\n')

def bashup():
    try:
        run('wget https://gist.githubusercontent.com/sgviking/7bb38938187e36308175/raw/a52b04a8a95af1b0251f866e068e1bdc0105bd2f/bashup_manual.sh')
        run('chmod +x bashup_manual.sh')
        sudo('export shasum=$(sha1sum bashup_manual.sh | cut -d" " -f1); if [[ "$shasum" == "eb0a7bacea4fbae22c7d850b6b27433048dcbeb0" ]]; then ./bashup_manual.sh; fi')
        sudo('rm -rf bash*')
    except:
        print('Could not connect and/or run bashup on this host.\n')

