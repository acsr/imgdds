# imgdds

A simple, cross-platform CLI tool to convert images **to/from DDS format**.

This tool uses imageio https://pypi.org/project/imageio/ 

# WARNING
This is under Development and NOT working yet!
Feel free to join development.

## about imageio
Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats. It is cross-platform, runs on Python 3.9+, and is easy to install.

Main website: https://imageio.readthedocs.io/


## 🔧 Install

Install via [uv](https://github.com/astral-sh/uv):

```bash
uv pip install 'git+https://github.com/acsr/imgdds.git'
```

Or using pip:

```bash
pip install 'git+https://github.com/acsr/imgdds.git'
```

## 🚀 Usage

```bash
imgdds input_path output_path [-r|--recursive]
```

- If `input_path` is a file, converts that file.
- If it's a directory, all supported files are converted.
- `--recursive` processes subdirectories.

## 🖼️ Examples

```bash
imgdds image.png output.dds
imgdds folder_of_pngs output_folder --recursive
imgdds texture.dds converted.png
```

Example dds image files can be downloaded from:
https://github.com/robertkist/py_dds/tree/main/example_images

## 📦 Supported Formats

- Input: PNG, JPG, BMP, DDS, etc.
- Output: PNG, JPG, DDS

## 📄 License

MIT
