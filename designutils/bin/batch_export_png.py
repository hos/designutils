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

def __main__():
    args = parser.parse_args()

    for fpath in args.files:
        pre, ext = os.path.splitext(fpath)
        cmd = ["inkscape", fpath, "--export-png="+pre+".png"]

        if args.dpi:
            cmd += ["--export-dpi="+args.dpi]

        print(">> "+" ".join(cmd))

        subprocess.call(cmd)


if __name__ == '__main__':
    __main__()
