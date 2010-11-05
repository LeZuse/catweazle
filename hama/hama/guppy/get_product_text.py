from profiles import profiles
from getter import BaseGetter

class HamaDescriptionsGetter(BaseGetter):
    def __init__(self, profile, code):
        BaseGetter.__init__(self, profile, code)
        self.code = code.zfill(8)
        self.post_values = profile.use_code(code)
        self.link_pattern = self.link_pattern % self.code


def main(code, supplier):
    
    hama_getter = HamaDescriptionsGetter(profiles.HAMA_DESCRIPTION, code)
    
    
    
    hama_getter.parse_link() 
    hama_getter.parse_description()
    output = hama_getter.dump_product_data()

    return output