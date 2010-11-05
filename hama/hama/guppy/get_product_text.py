import urllib, urllib2, re

from profiles import HAMA_DESCRIPTIONS

class Output(object):
    pass




class ResourceGetter(object):
    
    def __init__(self, profile, code):
        self.code = None
        self.link = None
        self.name = None
        self.remark = None
        self.description = None
        self.search_url = profile.search_url
        self.link_pattern = profile.link_pattern % code.zfill(8)
        self.name_pattern = profile.name_pattern
        self.description_pattern = profile.description_pattern
        self.post_values = profile.use_code(code)

    def parse_link(self):
        post_data = urllib.urlencode(self.post_values)
        request = urllib2.Request(self.search_url, post_data)	
        response = urllib2.urlopen(request)
        the_page = response.read()
        response.close()      
        # potentialy dangerous, if there's more than one result
        self.link = 'http://www.hama.de%s?lid=1' % re.findall(self.link_pattern, the_page)[0]
        self.code = re.findall('bySearch\*(.*)\?lid', self.link)[0]
        

    def parse_description(self):
        request = urllib2.Request(self.link)	
        response = urllib2.urlopen(request)
        the_page = response.read()
        response.close()     
        self.name = re.compile(self.name_pattern % self.code, re.MULTILINE).findall(the_page)[0]    
        self.description = self.description_pattern.findall(the_page)[0]	


    def dump_product_data(self):
        dump = Output()
        dump.code = self.code
        dump.link = self.link
        dump.name = self.name
        dump.remark = self.name
        dump.description = self.description 
        
        output = Output()
        output.data = dump
        output.name = ''
        output.format = 'txt'       
        return output

def main(code, supplier):
    
    hama_getter = ResourceGetter(HAMA_DESCRIPTIONS, code)
    hama_getter.parse_link() 
    hama_getter.parse_description()

    output = hama_getter.dump_product_data()

    return output