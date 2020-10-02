# Cloudflare Zones Scanner

The tool creates a list of DNS entries for all domains managed by Cloudflare.

## Usage

```commandline
usage: main [-h] [--xlsx-file XLSX_FILE] token

The tool creates a list of DNS entries for all domains managed by Cloudflare

positional arguments:
  token                 Cloudflare API Token with permission to read Zone and DNS entries

optional arguments:
  -h, --help            show this help message and exit
  --xlsx-file XLSX_FILE
                        The name of the resulting file in XLSX format
```

## Installation

The module uses additional packages that must be installed with the package installer for Python. To do this, run the command:

```commandline
pip install -r requirements.txt
```

or by using the make utility:

```commandline
make install
```

## Running the module

```commandline
python main TOKEN_HERE --xlsx-file=cloudflare.xlsx
```

## Virtual environment

The venv module provides support for creating "virtual environments" with your own independent set of Python packages. In order to prepare a virtual environment, we must first create it and then connect to it:

```commandline
python -m venv ./venv && source ./venv/Scripts/activate
```

or by using the make utility:

```commandline
make venv
```

**Instead of installing packages globally, we can only install them in a created virtual environment.**

In order to run the module with automatic connection to the virtual environment, the ``bin/run-venv.sh`` file has been prepared. Just run the command in the console:

```commandline
bin/run-venv.sh TOKEN_HERE --xlsx-file=cloudflare.xlsx
```

## License

MIT
