from fabric.context_managers import cd, shell_env
from fabric.operations import run, sudo


def step0(*args, **kwargs):
    with cd(kwargs.get("CWD", "$HOME")), shell_env(**kwargs.get("ENV", {})):
        return {
            k: tuple(v)
            for k, v in (
                ("run", list(map(run, kwargs["run"])) if "run" in kwargs else None),
                ("sudo", list(map(sudo, kwargs["sudo"])) if "sudo" in kwargs else None),
            )
            if v is not None
        }
