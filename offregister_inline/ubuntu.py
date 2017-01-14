from itertools import imap

from fabric.operations import sudo, run


def step0(*args, **kwargs):
    return {k: tuple(v)
            for k, v in (('run', imap(run, kwargs['run']) if 'run' in kwargs else None),
                         ('sudo', imap(sudo, kwargs['sudo']) if 'sudo' in kwargs else None))
            if v is not None}
