import re

profiles_data= {
    'HAMA_DESCRIPTION': {
        'name_pattern': r'<td class="itemErp">\r<h1>\r%s\r(.*)\r+</h1>',
        
        'search_url': 'http://www.hama.de/tools/advanced_search/index.hsp',
        
        'link_pattern': r"/portal/articleId\*\d+/action\*\d+/searchMode\*\d+/bySearch\*%s",
        
        'link_template': 'http://www.hama.de%s?lid=1',
        
        'description_pattern': re.compile(r'Highlights</h3>\r?\s*<div class="padding_1">\r?\s*<p>(.*)</p>', re.MULTILINE),
        
        'code_pattern': 'bySearch\*(.*)\?lid',
        
        'post_values': {'action': 1036, 'searchMode': 1, 'x': 0, 'y': 0},
        
        'output_format': 'txt'
        },
    
    
    
    'HAMA_IMAGE': {
        'search_url': 'http://172.16.132.202/webnative/searchengine?-f+-nohead+-nofoot+/aida1/accelerator/WebToPrint',
        
        'link_pattern': r"files\[\d+\] = new buildobject\((.*)\)",
        
        'post_values': '&'.join([
            'filenamelogic_0=0',
            'pathsearchtype_0=1',
            'filename_0=%s',        # code
            'filenamehasany_0=0',
            'filetype=1',
            'pathtype=3',
            'selectedvol=3',
            'skipcount=0',
            'maxmatches=100',   # maxmatches
            'action=search',
            'charset=undefined'
            ]),
        
        'username': 'hamaUK',
        
        'password': '14hama03'
        }
    }



class ProfilesContainer(object):
    pass

class Profile(object):    
    
    def __init__(self):
        self.settings = {}

    def use_code(self, code):
        post_values = self.settings['post_values']
        post_values['q'] = code.zfill(8)
        
        return post_values


profiles = ProfilesContainer()

for profile in profiles_data:
    
    new_profile = Profile()
    
    for entry in profiles_data[profile]:
        value = profiles_data[profile][entry]
        new_profile.settings[entry] = value
    
    setattr(profiles, profile, new_profile)




