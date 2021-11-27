import setuptools
from py_localtunnel.main import __version__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="py-localtunnel",
    version=__version__,
    author="Jak Bin",
    author_email="jakbin4747@gmail.com",
    description="localtunnel alternative in python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jakbin/py-localtunnel",
    install_requires=[""],
    python_requires=">=3",
    project_urls={
        "Bug Tracker": "https://github.com/jakbin/py-localtunnel/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    keywords='localtunnel,port-forwarding,expose-locahost',
    packages=["py_localtunnel"],
    entry_points={
        "console_scripts":[
            "pylt = py_localtunnel.main:main"
        ]
    }
)
