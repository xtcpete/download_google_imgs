import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="download_google_imgs",
    version="1.0.4",
    author="Gonglin Chen",
    author_email="xtcpetecgl@gmail.com",
    description="Python library to download images form Google Images with query.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xtcpete/download_google_imgs",
    keywords=['google', 'images', 'scraping', 'image download', 'bulk image downloader',],
    packages=['download_google_imgs'],
    requires = ["selenium", "tqdm", "beautifulsoup4"],
    classifiers=[
	"Programming Language :: Python :: 3",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
    ]
)