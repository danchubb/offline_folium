from urllib.request import urlopen, Request
import os

import folium
import folium.plugins as plugins 
from .paths import dest_path

def download_all_files():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    for _, js_url in folium.folium._default_js:
        download_url(js_url,js_url)
    for _, js_url in folium.folium._default_css:
        download_url(js_url,js_url)
    for plugin in plugins.__all__:   
        if hasattr(getattr(plugins,plugin),'default_js'):
            for _, js_url in getattr(plugins,plugin).default_js:
                req = Request(url=js_url, headers=headers) 
                download_url(js_url,req)          
        if hasattr(getattr(plugins,plugin),'default_css'):
            for _, js_url in getattr(plugins,plugin).default_css:
                req = Request(url=js_url, headers=headers)
                download_url(js_url,req)   


#added a url and d(ownload)url so that browser spoofing works where reauired for the plugins
def download_url(url,durl):
    output_path = os.path.join(dest_path, os.path.basename(url))
    print(f"Downloading {output_path}")
    contents = urlopen(durl).read().decode("utf8")
    with open(output_path, "w") as f:
        f.write(contents)

if __name__ == "__main__":
    print(f"Downloading files to {dest_path}")
    download_all_files()
