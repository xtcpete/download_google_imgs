import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="google_image_downloader",
    version="1.0.0",
    author="Gonglin Chen",
    author_email="xtcpetecgl@gmail.com",
    description="Python library to download images form Google Images with query.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gurugaurav/bing_image_downloader",
    keywords=['google', 'images', 'scraping', 'image download', 'bulk image downloader',],
    packages=['google_image_downloader'],
    classifiers=[
	"Programming Language :: Python :: 3",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
        ]
)