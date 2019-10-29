import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="studentui",
    version="0.2.1",
    author="kreny",
    author_email="kronerm9@gmail.com",
    description="A simple Qt application for fast access to Bakaláři school system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/23kreny/studentui",
    include_package_data=True,
    packages=["studentui"],
    entry_points={
        'gui_scripts': [
            'studentui = studentui.__init__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "PySide2",
        "bakalib >= 0.6.0"
    ]
)
