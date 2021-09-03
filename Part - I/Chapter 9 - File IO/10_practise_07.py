content = True

i = 1       # counter to count the no. of lines

with open('log_file.txt', 'r') as f:

    while content:              # will run as long as there is content and the value is True
        content = f.readline()  # reads one line at a time
        
        if 'python' in content.lower():         # lower() translates the whole file to lower case 
            print(f'Yes Python is present in line # {i}')
            print(content)

        i += 1
