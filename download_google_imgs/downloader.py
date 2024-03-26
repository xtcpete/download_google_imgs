from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from tqdm import tqdm
import os
from bs4 import BeautifulSoup
import re
import urllib.request as req
import os

class ImageFormatWarning(UserWarning):
    pass

class GoogleImageDownloader:
    def __init__(self, query, output_name=None, num_images=10, root_dir='images', add_ons=['4k']):
        """_summary_

        Args:
            query (_type_): query to search images
            output_name (_type_, optional): folder name for saving images. Defaults to None.
            num_images (int, optional): number of images to download. Defaults to 10.
            root_dir (str, optional): root directory for saving images. Defaults to 'images'.
            add_ons (list, optional): additional string for query. Defaults to ['4k'].
        """
        
        self.query = query
        
        if output_name is None:
            output_name = query.replace(' ', '_')
            
        self.output_name = output_name
        self.num_images = num_images
        self.root_dir = root_dir
        self.add_ons = add_ons
    
    def get_image(self, link):
        header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        raw_html = req.urlopen(req.Request(link, headers=header))
        soup = BeautifulSoup(raw_html, 'html.parser')
        img = soup.find_all('img',{"height":re.compile(r'\d+'), "width":re.compile(r'\d+')})[0].get('src')
        return img
    
    def download_img(self, img, data_path, img_id, verbose=True):
        header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        
        response = req.urlopen(req.Request(img, headers=header))
        raw_img = response.read()
        type = response.headers['Content-Type'].split('/')[1].lower()
    
        try:
            if type in ['jpeg', 'jpg', 'png']:
                with open(os.path.join(data_path, "{:08d}".format(img_id)+f'.{type}'), 'wb') as f:
                    f.write(raw_img)
            else:
                if verbose:
                    print(f"Image {img_id} is not in jpeg, jpg, or png format. Skipping...")
                return False
            return True
        except Exception as e:
            return False
        
    def download(self, get_urls=False, verbose=True):
        """_summary_

        Args:
            get_urls (bool, optional): if set to ture, it will only return links to images; images will not be downloaded. Defaults to False.

        Returns:
            _type_: links to images if get_urls is set to True, else None
        """
        
        
        options = Options()
        options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options)
    
        query_path = "https://www.google.com/search?q="+ self.query + ' ' + ' '.join(self.add_ons) +"&tbm=isch"
    
        driver.get(query_path)
        driver.implicitly_wait(3)
        actualImages = set()
    
        # create image directory
        if not os.path.exists(self.root_dir):
            os.mkdir(self.root_dir)
    
        data_path = os.path.join(self.root_dir, self.output_name)
    
        if not os.path.exists(data_path):
            os.mkdir(data_path)
    
        
        for i in range(self.num_images // 10):
            try:
                show_more = driver.find_elements(By.XPATH, '//input[@value="Show more results"]')
                show_more[0].click()
            except:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
             
        elements = driver.find_elements(By.XPATH, '//a[.//div[img] and not(@href)]')
        if elements == []:
            elements = driver.find_elements(By.XPATH, '//a[contains(@href, "imgres")]')

        if verbose:
            print(f"Found {len(elements)} images")
        
        links = []
        
        if verbose:
            print(f"Downloading {self.num_images} images")
            
        for e in elements[:self.num_images*2]:
            e.click()
            link = e.get_attribute('href')
            links.append(link)

        driver.quit()
        count = 1
        for i, link in enumerate(links):    
            if verbose:
                print(f"Downloading image {count}/{self.num_images}")
            img = self.get_image(link)
            if get_urls:
                actualImages.add(img)
            else:
                if self.download_img(img, data_path, i, verbose=verbose):
                    if verbose:
                        print(f'Image {count} downloaded to {data_path}')
                        count += 1
                if count >= self.num_images:
                    break
        
        if verbose:
            print(f"Done, Downloaded {count} images")
        
        if get_urls:
            return actualImages
        
        

def download(query, get_urls=False, output_name=None, num_images=10, root_dir='google_images', add_ons=['4k'], verbose=True):
    """_summary_

        Args:
            query (_type_): query to search images
            get_urls (bool, optional): if set to ture, it will only return links to images; images will not be downloaded. Defaults to False.
            output_name (_type_, optional): folder name for saving images. Defaults to query string.
            num_images (int, optional): number of images to download. Defaults to 10.
            root_dir (str, optional): root directory for saving images. Defaults to 'images'.
            add_ons (list, optional): additional string for query. Defaults to ['4k'].
            verbose (bool, optional): if set to True, it will print progress. Defaults to True.
        """
    downloader = GoogleImageDownloader(query, output_name, num_images, root_dir, add_ons)
    downloader.download(get_urls=get_urls, verbose=verbose)