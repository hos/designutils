import os
import glob
import sys
import argparse
import re
import subprocess

tmp_dir = "tmp"

parser = argparse.ArgumentParser()
parser.add_argument('files', type=str, nargs='+',
                    help='Files for replacement')
parser.add_argument("--dpi", type=str, help="Output DPI")
parser.add_argument("-o", "--output", type=str, required=True, help="Output pdf path")


def __main__():
    args = parser.parse_args()

    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    pdf_pages = []

    for fpath in args.files:
        dirname, filename = os.path.split(os.path.abspath(fpath))
        pre, ext = os.path.splitext(filename)
        output_fpath = os.path.join(tmp_dir, pre+".pdf")

        pdf_pages.append(output_fpath)

        cmd = ["inkscape", fpath, "--export-pdf="+output_fpath]

        if args.dpi:
            cmd += ["--export-dpi="+args.dpi]

        print(">> "+" ".join(cmd))

        subprocess.call(cmd)

    cmd = ["pdfunite"] + pdf_pages + [args.output]
    print(">> "+" ".join(cmd))
    subprocess.call(cmd)

if __name__ == '__main__':
    __main__()
