import sys
from download_google_imgs import downloader

query=sys.argv[1]
    
            
downloader.download(
    query,
    verbose=True,
)