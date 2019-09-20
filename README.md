# Myssh

Myssh is a ssh wrapper tool built with python.

## Installation
Use virtualenv to create a virtual enviroment for the tool

```bash
virtualenv -p python3 myssh
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install myssh.
 
```bash
pip install myssh
```

## Usage
```bash
$ con -h
usage: con [-h] name

positional arguments:
  name        name of server

optional arguments:
  -h, --help  show this help message and exit
```

```bash
$ sshentry -h
usage: sshentry [-h] [--host HOST] [--key_path KEY_PATH] [--user USER] name

positional arguments:
  name                  name you want to provide for server

optional arguments:
  -h, --help            show this help message and exit
  --host HOST, -s HOST  name of host
  --key_path KEY_PATH, -i KEY_PATH
                        path of key
  --user USER, -u USER  name of user
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
