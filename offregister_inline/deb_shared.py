# -*- coding: utf-8 -*-
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

    def unwrap_non_err(f):
        def get_out_of_non_err(res):
            return res.stdout if res.exited == 0 else res

        def inner(*args, **kwargs):
            return get_out_of_non_err(f(*args, **kwargs))

        return inner

    with c.cd(kwargs.get("CWD", "$HOME")):
        return {
            k: tuple(v)
            for k, v in (
                (
                    "run",
                    list(map(unwrap_non_err(runner), kwargs["run"]))
                    if "run" in kwargs
                    else None,
                ),
                (
                    "sudo",
                    list(map(unwrap_non_err(sudo_runner), kwargs["sudo"]))
                    if "sudo" in kwargs
                    else None,
                ),
            )
            if v is not None
        }


__all__ = ["inline0"]
