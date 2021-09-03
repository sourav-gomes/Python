words = ["donkey", "monkey", "cow"]

with open('donkey.txt', 'r') as f:
    txt = f.read()

for word in words:
    with open('donkey.txt', 'w') as f:    
        txt = txt.replace(word, '#@^#@&!')
        f.write(txt)