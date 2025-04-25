# Background Remover 🖼️✂️

A Python tool to remove backgrounds from images with a single command, using AI-powered segmentation.

<!-- ![Example](examples/output.png) -->

## Features

- 🚀 Fast background removal using U²-Net AI model
- 💻 Command-line interface
- 🖼️ Supports multiple image formats (JPG, PNG, etc.)
- ✨ Preserves transparency in output
- 📦 Lightweight and easy to integrate

## Installation

1. Clone the repository:
```bash
git clone https://github.com/iyoramu/python-bg-remover.git
cd python-background-remover
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python bgremover.py input.jpg
```

Specify output file:
```bash
python bgremover.py input.jpg -o output.png
```

Process all images in a folder (Linux/Mac):
```bash
for file in *.jpg; do python bgremover.py "$file"; done
```

## Requirements

- Python 3.6+
- See [requirements.txt](requirements.txt)

## API

You can also use this as a module:

```python
from bgremover import remove_background

remove_background("input.jpg", "output.png")
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

[MIT](LICENSE)
