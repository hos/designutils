from setuptools import setup, find_packages
from os import path
from setuptools.extension import Extension

here = path.abspath(path.dirname(__file__))

setup(
    name = "designutils",

    version = "0.0",

    description = "Design utils",

    author = "Onur Solmaz",

    author_email = "onursolmaz@gmail.com",

    packages = find_packages(exclude=["contrib", "docs", "tests"]),

    extras_require = {
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },

    # package_data={
    #     "sample": ["package_data.dat"],
    # },

    # data_files=[("my_data")],

    install_requires = {
        "numpy",
        "scipy",
    },

    # ext_modules = ""),

    entry_points = {
        "console_scripts": [
            "batch_export_png=designutils.bin.batch_export_png:__main__",
            "compile_pdf=designutils.bin.compile_pdf:__main__",
        ],
    },
)



