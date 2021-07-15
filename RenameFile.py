# encoding: utf-8 
#
# Copyright (c) 2021 https://github.com/realliyifei/
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2021-07-14
# 
# This program is to rename the input string following the small-case-with-hyphen format, 
# you can change it to other output formats as you want 

import sys
from workflow import Workflow3, ICON_INFO

# GitHub repo to check for updates
UPDATE_SETTINGS = {
    'github_slug': 'realliyifei/Alfred-File-Renamer'
}

# GitHub Issues
HELP_URL = 'https://github.com/realliyifei/Alfred-File-Renamer/issues'

# Global Parameters
connect_char = '-' # hyphen, you can also use underscore, space, etc. 
stripped_chars = [':', ',', '-', '_', '=', '+', '{', '}', '[', ']', '(', ')', 
                  '——', '：'] # the characheters to be stripped 

def main(wf):
    """Run the workflow"""
    # Update settings format
    if wf.update_available:
        # Add a notification to top of Script Filter results
        wf.add_item('Workflow update is available',
                    'Press ↩ or ⇥ to install',
                    autocomplete = 'workflow:update',
                    valid = False,
                    icon = ICON_INFO)
    
    # Main    
    try:
        filename = wf.args[0] 
        
        subtitle = "New Filename"
        renamed_filename = rename_filename(filename)
        wf.add_item(title = renamed_filename, subtitle = subtitle, arg = 'renamed_filename', valid = True)
        
    except:
        wf.add_item("Invalid input")
    
    wf.send_feedback() 

def rename_filename(filename):
    """
    Replaces the spaces in the query string with the connect character and strips the unnecessary character(s) 
    """
    for char in stripped_chars:
        filename = filename.replace(char, ' ')
    
    while True: 
        if filename[0] != ' ':
            break
        else:
            filename = filename[1:]
    
    # Removes all whitespace characters (space, tab, newline, return, formfeed)
    filename = " ".join(filename.split())
    
    filename = filename.lower()
    
    renamed_filename = filename.replace(' ', connect_char)
    
    return renamed_filename 
    

if __name__ == '__main__':
    # create a workflow3 object
    wf = Workflow3(
        update_settings = UPDATE_SETTINGS,
        help_url = HELP_URL,
    ) 
    sys.exit(wf.run(main)) 