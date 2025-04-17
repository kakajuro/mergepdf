# mergepdf

## Introduction
mergepdf is a simple CLI tool that merges multiple PDF files into a single PDF. Written in Python

## Usage
```bash
mergepdf pdf1.pdf pdf2.pdf output.pdf
```

You can merge multiple PDFs by listing them as arguments like this:
```bash
mergepdf file1.pdf file2.pdf file3.pdf output.pdf
```

They will be merged in the order you enter them as arguments

## Installation

### From Source
Clone the repository and run the Python file:
```bash
git clone https://github.com/kakajuro/mergepdf.git
cd mergepdf
python main.py
```

### Build from Source
To build from source:
```bash
make run-build
```

If you would like, you can use PyInstaller directly:
```bash
pyinstaller --onefile main.py
```

Note: PyInstaller must be installed for this to work. Install it using:
```bash
pip install pyinstaller
```

## Releases
You can download the latest executable from the [releases page](https://github.com/kakajuro/mergepdf/releases).

## License
MIT
