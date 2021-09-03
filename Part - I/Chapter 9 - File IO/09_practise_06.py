with open('log_file.txt', 'r') as f:
    txt = f.read()
    
    if 'python' in txt.lower():         # lower() translates the whole file to lower case 
        print('Yes Python is present')
    else:
        print('Yes Python is not present')
