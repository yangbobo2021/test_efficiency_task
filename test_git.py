

import random
import time
import os
from datetime import datetime

commit_index = 0
function_index = 0

def gen_fun_name():
    global commit_index
    global function_index
    function_index += 1

    return f'f_c{commit_index}_{function_index}'

def gen_function():
    return f'''
        void {gen_fun_name()}() {'{'}
            int a = 20;
            int b = 30;
            int i = 0;
            for (i=0; i<30; i++) {'{'}
                if (i>10) {'{'}
                    a += i;
                {'}'} else {'{'}
                    a += b;
                {'}'}
            {'}'}
        {'}'}
    '''

def gen_commit_file():
    global commit_index
    commit_index += 1

    fname = f'f_commit{commit_index}.c'

    with oepn(fname, 'w') as f:
        for i in range(0, 2000):
            f.write(gen_function())
    

def do_git():
    c1 = 'git add .'
    c2 = f'git commit -m "{time.time()}"'
    c3 = 'git push'

    os.system(c1)
    os.system(c2)
    os.system(c3)

for c in range(0, 4000):
    print('---> times:', c)
    gen_commit_file()
    do_git()
