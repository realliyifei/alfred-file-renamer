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

# Global Parameters
connect_char = '-' # hyphen, you can insteadly use underscore, space, etc. 
stripped_symbols = [':', ',', '-', '_', '+', '=', '?', '|', 
                    '{', '}', '[', ']', '(', ')', '<', '>'] # the symbols to be stripped 

def rename(filename):
    """
    Replaces the spaces in the query string with the connect character and strips the unnecessary character(s) 
    """
    for char in stripped_symbols:
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
    filename = ' '.join(sys.argv[1:])
    print(rename(filename))