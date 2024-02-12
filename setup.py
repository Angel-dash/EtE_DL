#creating a local packages instead of hosting online
import setuptools
#opening in read mode and assigning to varibales f 
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="EtE_DL"
AUTHOR_USER_NAME="Angel-dash"
SRC_REPO="EtE_DL"
AUTHOR_EMAIL="njlghmr@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python packgae for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    projects_urls={
        "bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)