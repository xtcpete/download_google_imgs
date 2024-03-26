import sys
from google_image_downloader import downloader

query=sys.argv[1]
    
            
downloader.download(
    query,
    verbose=True,
)