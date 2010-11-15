class Profile(object):
    
    def __init__(self):
        pass

    def use_code(self, code):
        post_values = self.post_values
        post_values['q'] = code.zfill(8)
        
        return post_values