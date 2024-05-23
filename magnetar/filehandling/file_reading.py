class FileReader:
    
    DELIMITER = ''
    
    def __init__(self):
        pass
    
    def read(self, file_string, file_ext):
        
        file_extensions = {
            'csv': self.read_csv,
            'zip': self.read_zip,
            'json': self.read_json
        }
        
        
        try:
            if file_ext in file_extensions:
                return file_extensions[file_ext](file_string)
        except: 
            pass
            
    def filter_badlines(self, file_string:str): 
        import numpy as np
               
        
        file_lines = np.array(file_string.split('\n'))

        detectdelim = DetectDelimiter()
        delimlines = np.array([detectdelim.detect_delimiter(l) for l in file_lines])

        delims, delimcounts = np.unique(delimlines, return_counts=True)

        countdelim_dict = dict(zip(delimcounts, delims))

        self.DELIMITER = countdelim_dict[np.max(delimcounts)]

        delim_mask = np.where(delimlines == self.DELIMITER, True, False)

        clean_csv_string = '\n'.join(list(file_lines[delim_mask]))
        
        return clean_csv_string
    
    def read_csv(self, file_string):
        from io import StringIO
        import pandas as pd
        
        filtered_lines = self.filter_badlines(file_string)
        
        df = pd.read_csv(StringIO(filtered_lines), sep = self.DELIMITER)

        return df
    
    def read_zip(self, zipfile):
        print("Unzip me")
        pass
    
    def read_json(self, file_string):
        
        import json
        from io import StringIO
        
        return json.loads(file_string)
    
    def read_excel(self, zipfile):
        pass
