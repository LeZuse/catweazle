import urllib, urllib2, re

class BaseGetter(object):
        
    def __init__(self, profile, code): 
        # whatever is in profile.settings dict
        # will create a new attribute
        for i in profile.settings:
            setattr(self, i, profile.settings[i])
        
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        
        if hasattr(self, 'username'):
            passman.add_password(None, self.base_url, self.username, self.password)
              
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)	
        self.opener = opener
        self.search_url = self.base_url + self.search_url


        
    def parse_links(self):        
        response = self.opener.open(self.search_url, data=self.post_values)
        the_page = response.read()
        response.close()      
        # potentialy dangerous, if there's more than one result
        self.links = re.findall(self.link_pattern, the_page)
  
        

    def dump_product_data(self):
        dump = self.Output()
        dump.code = self.code
        dump.links = self.links
        dump.name = self.name
        dump.remark = self.name
        dump.description = self.description         
        output = self.Output()
        output.data = dump
        output.name = ''
        output.format = self.output_format       
        return output
        
    class Output(object):
        pass        