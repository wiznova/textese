import os
import glob
import argparse
from pdf2image import convert_from_path
from PIL import Image


def convert_pdf_to_pngs_and_back(input_pdf, output_pdf, dpi):
    images = convert_from_path(input_pdf, dpi=dpi)

    images[0].save(
        output_pdf, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
    )


def main():
    parser = argparse.ArgumentParser(description="Truly flatten a pdf document.")
    parser.add_argument("input_pdf", type=str, nargs="?", help="Input PDF file path")
    parser.add_argument("output_pdf", type=str, nargs="?", help="Output PDF file path")
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="DPI setting for image quality (default: 150)",
    )
    parser.add_argument(
        "--all", action="store_true", help="Flatten all PDFs in the current directory"
    )
    parser.add_argument(
        "--outdir", type=str, default="./flattened", nargs="?", help="Output directory"
    )

    args = parser.parse_args()

    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    if args.all:
        for filename in glob.glob("*.pdf"):
            print(f"Converting: {filename}")
            convert_pdf_to_pngs_and_back(
                filename, os.path.join(args.outdir, filename), args.dpi
            )
    else:
        convert_pdf_to_pngs_and_back(
            args.input_pdf, os.path.join(args.outdir, args.output_pdf), args.dpi
        )


if __name__ == "__main__":
    main()
