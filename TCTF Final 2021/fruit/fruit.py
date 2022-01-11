#!/usr/bin/env python
# coding:utf-8

from tree_sitter import Language, Parser
from secret import flag
import time

MY_LANGUAGE = Language('./fruit.so', 'TCTF')


def banner():
    print('''                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                           #                    /                               
                          %%#    ##((          #%%                              
                    (####%%#%.   %%%#%*/     ####                               
                 (#####(#(##((&@&&&&@&&%##(%% &&&#(/                            
               ##(#(#    (#(%&&&&%%(/*/#((#%%(###/%& .#                         
              #(#    (##((&%%&(/#(###((/(((/#***#%#/(#%,                        
                   %#/##%%%%%(#(,(%(/*,#..,,,*.(*,#,# ,/%(                      
                 #(%%%*.%%%###/#/(,*%.%*.,#/*##*,.*#,/*/#/%                     
                .%*%%%%%%%( %(/*(,%#/,,/.%*,**,,#,(,(%#(%(%*                    
                #%%%%%#%%%##(*##%*,# %#,,/,*(*#.#,,#%*/#%*##                    
                /#%%%.%%%%(%(/(%%%#,*(###(/((((((#%*/(%(#%%/                    
                 %%/%%%%%%%%/%##%##%(*#(,#.###% (,,,(%%(%(%                     
                 *%%%#%%#,%#%%%%%((%%##%#**(,.#*/#%%#%#%%%(                     
                  %/%%(#%%%%%#(%%%%%#*(%#%%,,*/%%(%,%#%%(%                      
                   ##%%%%.%####%%*%%%%##,*%%(%%#/##%%*%#%                       
                     %##%%%%#%*(%%(%#(,%#/#(###/% *.(%*/                        
                      #/%%%#%%#%(%/*%#(,%#(##(%###%#%#                          
                        #(((%%%##%%((#%#/%%#%/##%(%%.                           
                         %*%#/#%/%#%#%(#%/##,%%##%%                             
                           #*#*#%#%%###%%%%*#%,##                               
                            *(%#%#%#(%*%%%,%*#%.                                
                              %###%#%##%###(#(                                  
                                 #%/#######                                     
                                                                                
                                                                                
                                                                                
                                                                                

        ''', flush=True)
    time.sleep(1)
    print('Welcome to TCTF fruit shop!', flush=True)
    time.sleep(1)
    for i in range(5):
        print('.', end='', flush=True)
        time.sleep(1)
    print('What\'s your favourite fruit?', flush=True)


if __name__ == '__main__':
    banner()
    parser = Parser()
    parser.set_language(MY_LANGUAGE)
    tree = parser.parse(flag.encode())
    root_node = tree.root_node
    r = root_node.sexp()
    if 'ERROR' not in r:
        if 'strawberry' in r:
            print('I love it!')
        else:
            print(':(')
