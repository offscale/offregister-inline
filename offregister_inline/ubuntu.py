from itertools import imap

from fabric.context_managers import shell_env, cd
from fabric.operations import sudo, run


def step0(*args, **kwargs):
    with cd(kwargs.get('CWD', '$HOME')), shell_env(**kwargs.get('ENV', {})):
        return {k: tuple(v)
                for k, v in (('run', imap(run, kwargs['run']) if 'run' in kwargs else None),
                             ('sudo', imap(sudo, kwargs['sudo']) if 'sudo' in kwargs else None))
                if v is not None}
