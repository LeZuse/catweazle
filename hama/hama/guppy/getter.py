import urllib, urllib2, re

class Output(object):
    pass

class BaseGetter(object):
    
    def __init__(self, profile, code):              
        for i in profile.settings:
            setattr(self, i, profile.settings[i])
        
        
    def parse_link(self):
        post_data = urllib.urlencode(self.post_values)
        request = urllib2.Request(self.search_url, post_data)	
        response = urllib2.urlopen(request)
        the_page = response.read()
        response.close()      
        # potentialy dangerous, if there's more than one result
        self.link = self.link_template % re.findall(self.link_pattern, the_page)[0]
        self.code = re.findall(self.code_pattern, self.link)[0]
        

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
        output.format = self.output_format       
        return output