# StalkPy

Command line tool to open the major social accounts connected to the specfic handle. Inspired from [HandleStalker](https://github.com/samanthakem/HandleStalker) :dancer: :rocket:

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/50ce8c28eb9d48afa53a544aa9f208d2)](https://www.codacy.com/app/vaibhavsingh97/StalkPy?utm_source=github.com&utm_medium=referral&utm_content=vaibhavsingh97/StalkPy&utm_campaign=Badge_Grade) [![Build Status](https://travis-ci.org/vaibhavsingh97/StalkPy.svg?branch=master)](https://travis-ci.org/vaibhavsingh97/StalkPy) [![Requirements Status](https://requires.io/github/vaibhavsingh97/StalkPy/requirements.svg?branch=master)](https://requires.io/github/vaibhavsingh97/StalkPy/requirements/?branch=master) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://vaibhavsingh97.mit-license.org/) <!-- https://github.com/jackton1/script_install -->

```
                     _____   _             _   _      _____          
                    / ____| | |           | | | |    |  __ \         
                    | (___  | |_    __ _  | | | | __ | |__) |  _   _
                    \___ \  | __|  / _` | | | | |/ / |  ___/  | | | |
                    ____) | | |_  | (_| | | | |   <  | |      | |_| |
                    |_____/  \__|  \__,_| |_| |_|\_\ |_|       \__, |
                                                                __/ |
                                                               |___/
```

## Installation

### Clone

**1.)** Clone the repository by using this link :

```
$ git clone https://github.com/vaibhavsingh97/StalkPy.git
```

### Run

**2.)** Open terminal window there and the type these comands :

```
$ cd Stalkpy && pip install -r requirements.txt
```

User can query as many username

```
$ python StalkPy.py -u USERNAME [USERNAME ...]
```

User can add URLS in configuration file

```
$ python StalkPy.py -a https://instagram.com,https://youtube.com
```

To get help use

```
$ python StalkPy.py [-h] [--help]
```

### Configure

**3.)** The `Config.json` contains a list of social accounts. You can add as many social accounts you want. Just remember to ensure the `Config.json` file is [valid JSON](http://jsonlint.com/).

### Support

|         | Python 2.7                      | Python 3.5                      |
|---------|---------------------------------|---------------------------------|
| Linux   | :white_check_mark: Full support | :white_check_mark: Full support |
| Max OS  | :white_check_mark: Full support | :white_check_mark: Full support |
| Windows | :white_check_mark: Full support | :white_check_mark: Full support |

#### To-do

- [ ] Make the script faster :)
- [ ] check list of browser and open accordingly
- [x] Command line addition of accounts to `Config.json`
- [ ] check the validity of username.
- [x] ~~handle case if no social account found~~
- [x] ~~test cross plateform support~~
- [x] ~~Add clint support (used argparse)~~

## Issues

You can report the bugs at the [issue tracker](https://github.com/vaibhavsingh97/StalkPy/issues)

## License

Built with ♥ by Vaibhav Singh([@vaibhavsingh97](https://github.com/vaibhavsingh97)) under [MIT License](https://vaibhavsingh97.mit-license.org/)

You can find a copy of the License at <https://vaibhavsingh97.mit-license.org/>
