
# coding: utf-8

# In[22]:

import glob

filelist = glob.glob('0*.md')
filelist.append('10-cmdline.md')


# In[23]:

def extract_code (filename):
    
    f = open(filename, 'r')

    code_block = False
    counter = 0

    for i,line in enumerate(f):
        # check to see if this is the start of a code block
        #print(code_block)
        #print(counter)

        if line == '~~~ {.python}\n':
            code_block = True
            counter = 1
        # if it's a code block, print the line, add "final" lines to counter
        if (code_block == True & counter < 2):
            print(line)
            if line == '~~~\n':
                counter = counter + 1
        # if the counter has been incremented twice (two endings), reset everything
        if(code_block == True & counter == 2):
            print("\n")
            code_block = False
            counter = 0
    f.close()


# In[26]:

for file in filelist:
    extract_code(file)


# In[ ]:



