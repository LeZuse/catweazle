"""TODO docstring"""

class BaseGetter(object):
    """TODO docstring"""        
    def __init__(self, profile, code): 
        
        # whatever is in profile.settings dict
        # will create a new attribute
        for i in profile.settings:
            setattr(self, i, profile.settings[i])


        # Create opener
        use_authentication = hasattr(self, 'username') and hasattr(self, 'password')
        do_not_use_authentication = not hasattr(self, 'username') and (not hasattr(self, 'password'))
        
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        if use_authentication:
            passman.add_password(None, self.base_url, self.username, self.password)
        elif do_not_use_authentication:
            pass
        else:
            raise ParseError, 'I need both username & password or none of them. Check your preferrences!'
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)

        
        # create additional attributes
        self.search_url = self.base_url + self.search_url
        self.opener = opener
        self.links = []


    def parse_links(self):   
        """TODO docstring"""
        response = self.opener.open(self.search_url, data=self.post_values)
        the_page = response.read()
        response.close()      
        self.links = re.findall(self.link_pattern, the_page)


    def dump_product_data(self):
        """TODO docstring"""
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
        """TODO docstring"""
        pass  
    
    
class ParseError(Exception):  
    """TODO docstring"""
    pass