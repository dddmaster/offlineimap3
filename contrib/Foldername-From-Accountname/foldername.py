from offlineimap.accounts import *

def get_folder_name(param=None):
  if isinstance(param,Account):
    return '/home/dddmaster/projects/imap/' + param.name
  return ''
