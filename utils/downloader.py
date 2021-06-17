import io
from zipfile import ZipFile

import requests

def zip_extract(file, target_path):
    if target_path == None:
        ZipFile(file).extractall()
    else:
        ZipFile(file).extractall(target_path)
    
class Downloader:
    _extract_funcs = {}
    _extract_funcs['zip'] = zip_extract
    

    @classmethod
    def get_extract_func(cls, ftype):
        return cls._extract_funcs.get(ftype)

    @classmethod
    def add_extract_func(cls, ftype, extract_func):
        cls._extract_funcs

    @staticmethod
    def get_filename_from_url(url):
        return url.split('/')[-1]

    @classmethod
    def run(cls, url, target_path=None,ftype=None):
        r = requests.get(url)
        extract = cls.get_extract_func(ftype)
        if extract is None:
            with open(target_path, 'wb') as f:
                f.write(r.content)
        else:
            extract(io.BytesIO(r.content),target_path)

if __name__ == "__main__":
    downloader = Downloader()
    downloader.run(ML_10M, './','zip')