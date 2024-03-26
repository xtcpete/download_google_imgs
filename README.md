![GitHub top language](https://img.shields.io/github/languages/top/gurugaurav/bing_image_downloader)
![GitHub](https://img.shields.io/github/license/gurugaurav/bing_image_downloader)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgurugaurav%2Fbing_image_downloader&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
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
pip install google_image_downloader
```

or 
```bash
git clone https://github.com/xtcpete/google_image_downloader
cd google_image_downloader
pip install -r requirements.txt
```


### Usage <br />
```python
from google_image_downloader import downloader
downloader.download(query, get_urls=False, output_name=None, num_images=10, root_dir='google_images', add_ons=['4k'], verbose=True)
```

`query (string)`: query to search images <br\>
`get_urls (bool, optional)`: if set to ture, it will only return links to images; images will not be downloaded. Defaults to False. <br\>
`output_name (string, optional)`: folder name for saving images. Defaults to query string. <br\>
`num_images (int, optional)`: number of images to download. Defaults to 1000.
`root_dir (str, optional)`: root directory for saving images. Defaults to 'images'. <br\>
`add_ons (list, optional)`: additional string for query. Defaults to ['4k']. <br\>
`verbose (bool, optional)`: if set to True, it will print progress. Defaults to True. <br\>


### PyPi <br />
https://pypi.org/project/bing-image-downloader/


</br>

