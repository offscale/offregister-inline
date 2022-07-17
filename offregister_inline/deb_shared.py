from functools import partial


def step0(c, *args, **kwargs):
    """
    :param c: Connection
    :type c: ```fabric.connection.Connection```
    """
    env = dict(**kwargs.get("ENV", {}))
    with c.cd(kwargs.get("CWD", "$HOME")):
        return {
            k: tuple(v)
            for k, v in (
                ("run", list(map(partial(c.run, env=env), kwargs["run"])) if "run" in kwargs else None),
                ("sudo", list(map(partial(c.sudo, env=env), kwargs["sudo"])) if "sudo" in kwargs else None),
            )
            if v is not None
        }


__all__ = ["step0"]
