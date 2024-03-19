import setuptools

# get the README file data for the long description 
with open('README.md', 'r') as file :
    long_description = file.read()

# read the the version number from the version file 
with open('config/VERSION.txt', 'r') as file :
    __version__ = file.read()


REPO_NAME = 'ml_template'
AUTHOR_USER_NAME = 'HarishKumarSedu'
SRC_REPO = 'mlProject'
AUTHOR_EMAIL = 'harishkumarsedu@gmail.com'

setuptools.setup(

    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='a small pytih ml project for the ml project templet',
    long_description= long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)