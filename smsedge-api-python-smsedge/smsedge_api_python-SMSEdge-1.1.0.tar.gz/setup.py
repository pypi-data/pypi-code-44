import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smsedge_api_python-SMSEdge", # Replace with your own username
    version="1.1.0",
    author="Mimon Copitman",
    author_email="mimon@smsedge.io",
    description="SMSEdge API package for Python development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SMSEdge/API-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    python_requires='>=3.6',
)