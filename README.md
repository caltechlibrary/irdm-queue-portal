# InvenioRDM Queue Portal

This repository consists the automation to build a table of content currently
in an InvenioRDM community queue. It extracts `@tags` and presents them in a
browsable interface. It runs entirely using GitHub actions and GitHub pages.

[![License](https://img.shields.io/badge/License-BSD--like-lightgrey)](https://choosealicense.com/licenses/bsd-3-clause)
[![Latest release](https://img.shields.io/github/v/release/caltechlibrary/template.svg?color=b44e88)](https://github.com/caltechlibrary/template/releases)
[![DOI](https://data.caltech.edu/badge/201106666.svg)](https://data.caltech.edu/badge/latestdoi/201106666)


## Table of contents

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Known issues and limitations](#known-issues-and-limitations)
* [Getting help](#getting-help)
* [Contributing](#contributing)
* [License](#license)
* [Authors and history](#authors-and-history)
* [Acknowledgments](#authors-and-acknowledgments)


## Introduction

This project provides a more navicable queue view for users. While it could
have been developed inside of InvenioRDM, this approach was easier and more
flexible.

## Installation

This portal has only been tested with the CaltechAUTHORS repository and is
designed for use at Caltech. Please let us know if you're interested in using
it elsewhere and we can make it more flexible. For caltech users, you need to 
have a CaltechAUTHORS access token set in the CTATOK environment variable or as 
a GitHub repo secret.

## Usage

You can harvest and render the table by [golng
here](https://github.com/caltechlibrary/irdm-queue-portal/actions/workflows/render.yaml)
and clicking the "Run Workflow" button.

## Known issues and limitations

This tool is designed for use at Caltech and has some hardcoded URLs. Let us
know if you're interested in using it elsewhere.

## Getting help

Please open an issue on GitHub

## Contributing

Pull requests are highly encouraged.

## License

Software produced by the Caltech Library is Copyright © 2023 California Institute of Technology.  This software is freely distributed under a BSD-style license.  Please see the [LICENSE](LICENSE) file for more information.


## Authors and history

Tom Morrell created this project.

## Acknowledgments

This work was funded by the California Institute of Technology Library.

<div align="center">
  <br>
  <a href="https://www.caltech.edu">
    <img width="100" height="100" src="https://raw.githubusercontent.com/caltechlibrary/template/main/.graphics/caltech-round.png">
  </a>
</div>
