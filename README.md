# config_io

[![License](https://img.shields.io/badge/license-Custom--SA-%231b25e5)](https://raw.githubusercontent.com/Python-Components-Group/config_io/refs/heads/main/LICENSE)

A Python component that provides loading/saving services for dict-like configuration files for every Python software

## Component Description

This Python component is built by 2 sub-components (or software modules):
- **<u>config_parser</u>** which provides the service to parse configuration files and load them into memory
- **<u>config_validator</u>** which provides the service to validate the semantics of a configuration file read to check if it conforms to a well-defined schema

### Types of configuration files supported

As said, the configuration files supported are configuration files that can be **represented, conceptually, with a dictionary data structure**.

This means that every format that can represent the configuration data in a conceptual "dictionary form" can be implemented as a parser.<br/>
Validators implies no particular restrictions instead, so, virtually, configuration files with any purpose can be implemented.

## Component Dependencies

- [path_validator](https://github.com/Python-Components-Group/path_validator/) (Python Component)

## How to get the component

### Latest stable release

You can find the binaries of the component in the [release](https://github.com/Python-Components-Group/config_io/releases) section of this repository

### Latest build

#### Installation

```python
pip install git+https://github.com/Python-Components-Group/config_io
```

#### Update

```python
pip install git+https://github.com/Python-Components-Group/config_io --upgrade
```
