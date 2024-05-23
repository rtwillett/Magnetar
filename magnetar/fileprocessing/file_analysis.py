class DetectDelimiter:
    
    def __init__(self, pref_delim = []):
        
        if pref_delim == []:
            self.delim = [':', ';', '|', ',', '\t', ' ']
        else: 
            self.delim = pref_delim
            
    def detect_delimiter(self, s:str):

        import csv
        sniffer = csv.Sniffer()
        sniffer.preferred = [':', ';', '|', ',', '\t', ' ']

        try:

            dialect = sniffer.sniff(s)
            return dialect.delimiter
        except:
            return ''



