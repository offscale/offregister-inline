offregister_inline
===============

## Install package

    pip install .

## Example use in offregister JSON

    {
        "module": "offregister-inline",
        "kwargs": {
          "sudo": [
            "echo sudo USER=$USER",
            "echo sudo USER=$USER"
          ],
          "run": [
            "echo run USER=$USER",
            "echo run USER=$USER"
          ]
        }
    }
