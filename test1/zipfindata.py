import os
import shutil

for name in os.listdir('/home/hanwa/temp/678299_csv/'):
    shutil.make_archive('/home/hanwa/git/data/finance/hist1/'+name, 'zip', '/home/hanwa/temp/678299_csv/'+name)
    print(name)