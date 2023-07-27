# Textidy

## Overview

Textidy is a powerful and easy-to-use Python package for preparing PDF files for various use cases. It streamlines your PDFs by flattening them, which reduces their complexity and makes them easier to work with. Use cases include document preparation for OCR, removing interactive elements, document archiving, preparing documents for printing, and more.

## Installation

First, ensure you have Python 3.7+ installed on your system. You can verify this by running:

```bash
python3 --version
```

Next, you need to install Poetry, which is the package manager Textidy uses:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

For more detailed installation instructions for Poetry, refer to the [official Poetry documentation](https://python-poetry.org/docs).

You'll also need to install [Poppler](https://poppler.freedesktop.org/), which is a dependency for the `pdf2image` package:

On Ubuntu:

```bash
sudo apt-get install -y poppler-utils
```

On MacOS:

```bash
brew install poppler
```

Once you have Poetry and `poppler-utils` installed, you can install Textidy:

```bash
poetry install
```

This command creates a virtual environment and installs the necessary dependencies in it.

## Usage

You can use Textidy from the command line:

```bash
flatten --input <input_filename> --output <output_filename> --dpi <dpi>
```

Replace `<input_filename>`, `<output_filename>`, and `<dpi>` with your desired input filename, output filename, and DPI setting (default is 150).

There's also an option to flatten all the PDFs in the current directory:

```bash
flatten --all
```

## Development

If you want to make changes to the code and test them, you can install the package in editable mode. This means that changes to the source code will be immediately reflected in the installed package without needing to rebuild and reinstall:

```bash
make
```

Note that this command needs to be run in the virtual environment created by Poetry. You can activate it with `poetry shell`.

## Licensing

This software is dual-licensed.

1. **For non-commercial use**: This software is available under the terms of the GNU Affero General Public License (AGPL). See the `LICENSE` file and `LICENCE.txt` for the full text of this license. 

2. **For commercial use**: If you want to use this software for commercial purposes, you'll need a separate license. Please contact the author for more information. 

## Contact

For inquiries about commercial licensing, please contact me at:

Sergey Khalil
license@sergeykhalil.com