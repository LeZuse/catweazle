"""TODO docstring"""

import re, os
from hama.guppy.profiles import profiles
from hama.guppy.getter import BaseGetter
# from PIL import Image
# from cStringIO import StringIO

class HamaImagesGetter(BaseGetter):
    """TODO docstring"""
    def __init__(self, profile, code):
        BaseGetter.__init__(self, profile, code)
        
        self.code = code.zfill(8)
        self.post_values = self.post_values % self.code
        
        self.packshot_urls = []
        self.image_urls = []
        self.pdf_urls = []
        self.fallback_urls = []

    
    def parse_links(self):
        BaseGetter.parse_links(self)
        links = self.links
        
        # remove quotes
        links = [re.sub('\'', '', i).split(',') for i in self.links]
        
        # filter matches begining with 0 or 730
        condition = r'^(730+|0*)' + self.code + '\D.*'
        links = [link[1] for link in links if re.search(condition, link[0])]
        
        # merge matches with thw link template
        links = [self.link_template % link for link in links] 
        
        # convert to tuple of uniques
        links = tuple(set(links))
          

        self.links = links
        
        
        
#         adresses = []
# 
#         
#         
#         for i in self.links:
#             if True: #re.search(r'^(730+|0*)' + self.code + '\D.*', i[0]):
#                 adresses.append(self.link_template % i)
	
	

        
        for row in self.links:
            extension = os.path.splitext(row)[1][1:].upper()            
            
            has_unwanted_suffix = re.search(self.unwanted_suffices, row[0])
            if extension == "EPS" and not has_unwanted_suffix:
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
                self.pdf_urls.append(self.pdf_link_template + row[1])
    
            elif extension == "1":
                self.packshot_urls.append(self.link_template + row[1])
                
            else:
                pass

    def download_images(self):
        """TODO docstring"""
        page = self.opener.open(self.image_urls[1])
        image_data = page.read()
        page.close()
        
#        image_data = Image.open(StringIO(image_data))
#        print 'X: %s Y: %s' % image_data.size

def main(code, supplier):
    """TODO docstring"""
    hama_getter = HamaImagesGetter(profiles.HAMA_IMAGE, code)   
    
    hama_getter.parse_links() 
    print hama_getter.image_urls
    # hama_getter.download_images()

