
import re

#Parte uno
pattern = "\s(\d+).\s+(\d+).\s+(\d+).*"
mint = 99999
day = 0
for i, line in enumerate(open('weather.dat')):
    match=re.search(pattern, line)
    if match:
        newMin = int(match.group(2))-int(match.group(3))
        if mint > newMin:
            mint = newMin
            day = match.group(1)
print day

#Parte dos
pattern = "\d+\.\s(\w+).*(\s\d+)\s*-\s+(\d+)*"
mint = 99999
day = 0
for i, line in enumerate(open('football.dat')):
    match=re.search(pattern, line)
    if match:
        newMin = int(match.group(2))-int(match.group(3))
        if mint > newMin:
            mint = newMin
            day = match.group(1)
print day

#Parte tres
def general(patern, file):
    mint = 99999
    day = 0
    for i, line in enumerate(open(file)):
        match=re.search(patern, line)
        if match:
            newMin = int(match.group(2))-int(match.group(3))
            if mint > newMin:
                mint = newMin
                day = match.group(1)
    print day

#Llamadas al metodo general
general('\s(\d+).\s+(\d+).\s+(\d+).*', 'weather.dat')
general('\d+\.\s(\w+).*(\s\d+)\s*-\s+(\d+)*', 'football.dat')
