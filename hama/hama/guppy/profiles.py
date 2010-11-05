import re

class Profile(object):
    def use_code(self, code):
        post_values = self.post_values
        post_values['q'] = code.zfill(8)
        
        return post_values


HAMA_DESCRIPTIONS = Profile()
HAMA_DESCRIPTIONS.search_url = 'http://www.hama.de/tools/advanced_search/index.hsp'
HAMA_DESCRIPTIONS.link_pattern = r"/portal/articleId\*\d+/action\*\d+/searchMode\*\d+/bySearch\*%s"
HAMA_DESCRIPTIONS.name_pattern = r'<td class="itemErp">\r<h1>\r%s\r(.*)\r+</h1>'
HAMA_DESCRIPTIONS.description_pattern = re.compile(r'Highlights</h3>\r?\s*<div class="padding_1">\r?\s*<p>(.*)</p>', re.MULTILINE)
HAMA_DESCRIPTIONS.post_values = {'action': 1036, 'searchMode': 1, 'x': 0, 'y': 0}