class FileGetRequest:
    
    def __init__(self):
        pass
    
    def get_file(self, url):
        
        self.file_ext = self.detect_filetype(url)
        self.data = self.get_data(url)
    
    def detect_filetype(self, url:str):
        
        filetypes = [
            'csv',
            'txt',
            'json',
            'xlsx',
            'zip'
        ]
            
        try:
            file_ext = url.split('.')[-1].lower()
            if len(file_ext) < 6:
                return file_ext
            elif len(file_ext) >=6:
                for ft in filetypes:
                    if ft in file_ext:
                        return ft
                    else: 
                        return ''
            else: 
                return ''
        except:
            return ''
    
    def get_data(self, url):
        import requests
        
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(url, headers = headers)
        recs = r.text
        return recs



