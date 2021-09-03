f = open('another.txt', 'w')
f.write('Please write this to the file...')
# f.write('Please write this to the file... AGAIN')   # this will overwrite the previous write (NOT append)
f.close()
## IMP: If you execute the above write() statements consecutively (as above 2) it will append the 2nd statement after the first
f = open('another.txt', 'w')
f.write('Please write this to the file... AGAIN')
f.close()
##  But if you execute the above write() statements separately (i.e. open after closing), it will overwrite the previous content.
