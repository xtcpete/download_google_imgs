## Google Image Downloader
<hr>

Simple Python package to download images form Google Images with query.
This package selenium webdriver to retrive links to high resolution images<br/>

### Disclaimer<br />

This package helps you download images from Google Image.
This package can download up to around 800-1000 images, depending the number of images return for a given query.
Please do not violate any its terms. 

### Installation <br />
```sh
pip install download_google_imgs
```

or 
```bash
git clone https://github.com/xtcpete/download_google_imgs
cd download_google_imgs
pip install -r requirements.txt
```


### Usage <br />
```python
from download_google_imgs import downloader
downloader.download(query, get_urls=False, output_name=None, num_images=10, root_dir='google_images', add_ons=['4k'], verbose=True)
```

`query (string)`: query to search images <br\ >
`get_urls (bool, optional)`: if set to ture, it will only return links to images; images will not be downloaded. Defaults to False. <br\ >
`output_name (string, optional)`: folder name for saving images. Defaults to query string. <br\ >
`num_images (int, optional)`: number of images to download. Defaults to 1000.
`root_dir (str, optional)`: root directory for saving images. Defaults to 'images'. <br\ >
`add_ons (list, optional)`: additional string for query. Defaults to ['4k']. <br\ >
`verbose (bool, optional)`: if set to True, it will print progress. Defaults to True. <br\ >


### PyPi <br />
https://pypi.org/project/download-google-imgs/


</br>

