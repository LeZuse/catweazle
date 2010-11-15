import urllib, urllib2, re

from profiles import profiles
from getter import BaseGetter

class HamaDescriptionsGetter(BaseGetter):
    def __init__(self, profile, code):
        BaseGetter.__init__(self, profile, code)
        self.code = code.zfill(8)
        self.post_values = self.post_values % self.code
        self.link_pattern = self.link_pattern % self.code


    def parse_links(self):
        BaseGetter.parse_links(self)
        self.links = tuple(set([self.link_template % link for link in self.links]))
        self.code = re.findall(self.code_pattern, self.links[0])[0] 


    def parse_description(self):
        response = self.opener.open(self.links[0])
        the_page = response.read()
        response.close()     
        self.name = re.compile(self.name_pattern % self.code, re.MULTILINE).findall(the_page)[0]    
        self.description = self.description_pattern.findall(the_page)[0]


def main(code, supplier):
    hama_getter = HamaDescriptionsGetter(profiles.HAMA_DESCRIPTION, code)
    hama_getter.parse_links() 
    hama_getter.parse_description()
    output = hama_getter.dump_product_data()
    
    print '\n'.join(output.data.links)
    
    return output