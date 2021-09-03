# My way of solving problem #4 

with open('donkey.txt', 'r') as f:
    txt = f.read()
with open('donkey.txt', 'w') as f:    
    txt = txt.replace('donkey', '######')
    f.write(txt)