<!--
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** um-identity-setup
-->

<!-- PROJECT SHIELDS -->
<!--
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
![Build][build-shield]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/EOEPCA/um-identity-setup">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">um-identity-setup</h3>

  <p align="center">
    Scripts to set up the Identity.
    <br />
    <a href="https://github.com/EOEPCA/um-identity-setup"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/EOEPCA/um-identity-setup">View Demo</a>
    ·
    <a href="https://github.com/EOEPCA/um-identity-setup/issues">Report Bug</a>
    ·
    <a href="https://github.com/EOEPCA/um-identity-setup/issues">Request Feature</a>
  </p>
</p>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
    - [Built With](#built-with)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Testing](#testing)
- [Documentation](#documentation)
- [Usage](#usage)
    - [Running the template service](#running-the-template-service)
    - [Upgrading Gradle Wrapper](#upgrading-gradle-wrapper)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->

## About The Project


Includes scripts to set up the Identity:

- Registers default realms
- Registers default users
- Registers needed clients
- Registers default resources

### Built With

- [Python](https://www.python.org//)
- [PyTest](https://docs.pytest.org)
- [YAML](https://yaml.org/)
- [Travis CI](https://travis-ci.com/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org//)

### Installation

1. Get into EOEPCA's development environment

```sh
vagrant ssh
```

2. Clone the repo

```sh
git clone https://github.com/EOEPCA/um-identity-setupgit
```

3. Change local directory

```sh
cd um-identity-setup
```

### Build and Execute

Local:

```shell
pip install -r .\requirements.txt
python src/main.py
```

Docker:

```shell
docker build -f identity-setup/Dockerfile . -t identity-setup
docker run -d --name identity-setup identity-setup
```

## Documentation

The component documentation can be found at https://eoepca.github.io/um-identity-setup/.

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/EOEPCA/um-identity-setup/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the Apache-2.0 License. See `LICENSE` for more information.

## Contact

[EOEPCA mailbox](eoepca.systemteam@telespazio.com)

Project Link: [https://github.com/EOEPCA/um-identity-setup](https://github.com/EOEPCA/um-identity-setup)

## Acknowledgements

- README.md is based on [this template](https://github.com/othneildrew/Best-README-Template) by [Othneil Drew](https://github.com/othneildrew).

[contributors-shield]: https://img.shields.io/github/contributors/EOEPCA/um-identity-setupsvg?style=flat-square
[contributors-url]: https://github.com/EOEPCA/um-identity-setup/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EOEPCA/um-identity-setupsvg?style=flat-square
[forks-url]: https://github.com/EOEPCA/um-identity-setup/network/members
[stars-shield]: https://img.shields.io/github/stars/EOEPCA/um-identity-setupsvg?style=flat-square
[stars-url]: https://github.com/EOEPCA/um-identity-setup/stargazers
[issues-shield]: https://img.shields.io/github/issues/EOEPCA/um-identity-setupsvg?style=flat-square
[issues-url]: https://github.com/EOEPCA/um-identity-setup/issues
[license-shield]: https://img.shields.io/github/license/EOEPCA/um-identity-setupsvg?style=flat-square
[license-url]: https://github.com/EOEPCA/um-identity-setup/blob/master/LICENSE
[build-shield]: https://www.travis-ci.com/EOEPCA/um-identity-setupsvg?branch=master
