ciag = "wi!@ewiórka feoifeg egwgge egegegge"
znaki = (',', '.', ' ', '!', '@')
zamiana = ""
ciagret = ''
for znak in ciag:
    for znspec in znaki:
        if znak == znspec:
            #ciagret += znak
            break
    else:
        ciagret += znak
    # if znak not in znaki: ciagret += znak
    # else: ciagret += zamiana
print(ciagret)