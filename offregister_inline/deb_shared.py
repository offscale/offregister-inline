from functools import partial


def inline0(c, *args, **kwargs):
    """
    Run `run` and/or `sudo` commands with `&&` condition

    :param c: Connection
    :type c: ```fabric.connection.Connection```
    """
    env = dict(**kwargs.get("ENV", {}))
    runner = partial(c.run, env=env)
    sudo_runner = partial(c.sudo, env=env)
    with c.cd(kwargs.get("CWD", "$HOME")):
        return {
            k: tuple(v)
            for k, v in (
                (
                    "run",
                    list(map(runner, kwargs["run"])) if "run" in kwargs else None,
                ),
                (
                    "sudo",
                    list(map(sudo_runner, kwargs["sudo"]))
                    if "sudo" in kwargs
                    else None,
                ),
            )
            if v is not None
        }


__all__ = ["inline0"]
