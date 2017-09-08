import os
import glob
import sys
import argparse
import re
import subprocess

dir_option = "dir"
ext_option = "ext"

parser = argparse.ArgumentParser()
parser.add_argument('files', type=str, nargs='+',
                    help='Files for replacement')
parser.add_argument("--dpi", type=str, help = "Output DPI")
parser.add_argument("-o", "--output", type=str, help = "Output directory")

def __main__():
    args = parser.parse_args()

    if args.output:
        if not os.path.exists(args.output):
            os.makedirs(args.output)


    for fpath in args.files:
        pre, ext = os.path.splitext(fpath)
        filename = pre+".png"

        if args.output:
            opath = os.path.join(args.output, filename)
        else:
            opath = filename

        cmd = ["inkscape", fpath, "--export-png="+opath]

        if args.dpi:
            cmd += ["--export-dpi="+args.dpi]

        print(">> "+" ".join(cmd))

        subprocess.call(cmd)


if __name__ == '__main__':
    __main__()
