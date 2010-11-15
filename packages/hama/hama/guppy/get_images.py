import urllib2, re, os
import pdb
from profiles import profiles
from getter import BaseGetter
from PIL import Image
from cStringIO import StringIO

class HamaImagesGetter(BaseGetter):
    def __init__(self, profile, code):
        BaseGetter.__init__(self, profile, code)
        
        self.unwanted_suffices = self.unwanted_suffices.split(':')
        self.code = code.zfill(8)
        self.post_values = self.post_values % self.code
        
        self.packshot_urls = []
        self.image_urls = []
        self.pdf_urls = []
        self.fallback_urls = []

    
    def parse_links(self):
        BaseGetter.parse_links(self)
        
        self.links = [re.sub('\'', '', i).split(',') for i in self.links]
        self.links = tuple(set([self.link_template % link[1] for link in self.links if re.search(r'^(730+|0*)' + self.code + '\D.*', link[0])]))
        
        
        
#         adresses = []
# 
#         
#         
#         for i in self.links:
#             if True: #re.search(r'^(730+|0*)' + self.code + '\D.*', i[0]):
#                 adresses.append(self.link_template % i)
	
	

        
        for row in self.links:
            extension = os.path.splitext(row)[1][1:].upper()            
            
            
            if extension == "EPS" and not re.search('|'.join(self.unwanted_suffices), row[0]):
                if re.search('ver', row[0]):
                    self.packshot_urls.append(self.link_template + row[1])
                else:
                    self.image_urls.append(row)
            
            elif extension == "JPG":
                if re.search('qvp', row[0]):
                    self.packshot_urls.append(self.link_template + row[1])
                
                elif re.search('x', row[0]):
                    self.fallback_urls.append(self.link_template + row[1])
            
            elif extension == "PDF":
                self.pdf_urls.append('http://172.16.132.202/webnative/getimage?-f+maczip+-high+' + row[1])
    
            elif extension == "1":
                self.packshot_urls.append(self.link_template + row[1])
                
            else:
                pass

    def download_images(self):
        page = self.opener.open(self.image_urls[1])
        image_data = page.read()
        page.close()
        
        image_data = Image.open(StringIO(image_data))
        print 'X: %s Y: %s' % image_data.size

def main(code, supplier):
    
    hama_getter = HamaImagesGetter(profiles.HAMA_IMAGE, code)   
    
    hama_getter.parse_links() 
    print hama_getter.image_urls
    # hama_getter.download_images()

