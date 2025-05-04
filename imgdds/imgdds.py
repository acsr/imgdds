import argparse
from pathlib import Path
from PIL import Image
import imageio.v3 as iio

def convert_image(input_path: Path, output_path: Path):
    ext = output_path.suffix.lower()
    if ext == '.dds':
        img = Image.open(input_path)
        iio.imwrite(output_path, img)
    elif input_path.suffix.lower() == '.dds':
        img = iio.imread(input_path)
        img = Image.fromarray(img)
        img.save(output_path)
    else:
        img = Image.open(input_path)
        img.save(output_path)
    print(f"[✓] Converted: {input_path} -> {output_path}")

def find_images(input_dir: Path, recursive: bool):
    pattern = '**/*' if recursive else '*'
    for path in input_dir.glob(pattern):
        if path.is_file():
            yield path

def main():
    parser = argparse.ArgumentParser(description="Convert images to/from DDS format.")
    parser.add_argument("input", type=Path, help="Input file or directory")
    parser.add_argument("output", type=Path, help="Output file or directory")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively process directories")
    args = parser.parse_args()

    if args.input.is_file():
        args.output.parent.mkdir(parents=True, exist_ok=True)
        out_ext = '.dds' if args.input.suffix != '.dds' else '.png'
        out_path = args.output if args.output.suffix else args.output.with_suffix(out_ext)
        convert_image(args.input, out_path)

    elif args.input.is_dir():
        args.output.mkdir(parents=True, exist_ok=True)
        for file in find_images(args.input, args.recursive):
            rel_path = file.relative_to(args.input)
            out_ext = '.dds' if file.suffix.lower() != '.dds' else '.png'
            target_file = args.output / rel_path.with_suffix(out_ext)
            target_file.parent.mkdir(parents=True, exist_ok=True)
            convert_image(file, target_file)

    else:
        print("[!] Invalid input path.")
