# Problem # 11: Rename a file > 'renamed_by_python.txt'

import os       # has function os.remove() to delete files

oldfilenm = "sample2.txt"
newfilenm = "renamed_by_python.txt"

with open(oldfilenm) as f:
    content = f.read()  

with open(newfilenm, 'w') as f:
    f.write(content)  

os.remove(oldfilenm)