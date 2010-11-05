import urllib2, re, os
from profiles import profiles
from getter import BaseGetter

class HamaImagesGetter(BaseGetter):
    def __init__(self, profile, code):
        BaseGetter.__init__(self, profile, code)
        self.code = code.zfill(8)
        self.post_values = self.post_values % self.code
        
        self.packshot_urls = []
        self.image_urls = []
        self.pdf_urls = []
        self.fallback_urls = []

        XINET_address =  'http://172.16.132.202'
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, XINET_address, self.username, self.password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)	
        self.opener = opener
        
    
    def parse_links(self):
        page = self.opener.open(self.search_url, data=self.post_values)
        page_data = page.read()
        search_result = re.findall(r"files\[\d+\] = new buildobject\((.*)\)", page_data)
        
        search_result  = [re.sub('\'', '', i).split(',') for i in search_result]
        adresses = []
        unwanted_suffices = ['ean', 'tes', 'uap', 'str', 'mke'	]
        image_address = 'http://172.16.132.202/webnative/imageorder?-g+-xjpg90+-v+-crgb+'
        
        
        for i in search_result:
            if re.search(r'^(730+|0*)' + self.code + '\D.*', i[0]):
                adresses.append([i[0], i[1]])
	
        for row in adresses:
            extension = os.path.splitext(row[0])[1][1:].upper()            
            
            if extension == "EPS" and not re.search('|'.join(unwanted_suffices), row[0]):
                if re.search('ver', row[0]):
                    self.packshot_urls.append(image_address + row[1])
                else:
                    self.image_urls.append(image_address + row[1])
            
            elif extension == "JPG":
                if re.search('qvp', row[0]):
                    self.packshot_urls.append(image_address + row[1])
                
                elif re.search('x', row[0]):
                    self.fallback_urls.append(image_address + row[1])
            
            elif extension == "PDF":
                self.pdf_urls.append('http://172.16.132.202/webnative/getimage?-f+maczip+-high+' + row[1])
    
            elif extension == "1":
                self.packshot_urls.append(image_address + row[1])
                
            else:
                pass


def main(code, supplier):
    
    hama_getter = HamaImagesGetter(profiles.HAMA_IMAGE, code)   
    hama_getter.parse_links() 
    print '\n'.join(hama_getter.fallback_urls)

