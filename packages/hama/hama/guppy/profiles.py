import re
import os
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read(os.path.expanduser('~/.guppy.ini'))

profiles_data = {}

for section in config.sections():
    profiles_data[section] = {}
    for option in config.options(section):
        
         profiles_data[section][option] = config.get(section, option)


profiles_data['HAMA_DESCRIPTION']['description_pattern'] = re.compile(profiles_data['HAMA_DESCRIPTION']['description_pattern'], re.MULTILINE)





class ProfilesContainer(object):
    pass

class Profile(object):    
    
    def __init__(self):
        self.settings = {}




profiles = ProfilesContainer()

for profile in profiles_data:
    
    new_profile = Profile()
    
    for entry in profiles_data[profile]:
        value = profiles_data[profile][entry]
        new_profile.settings[entry] = value
    
    setattr(profiles, profile, new_profile)




