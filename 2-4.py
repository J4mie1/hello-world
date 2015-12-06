__author__ = 'jamie'

import numpy as np
import matplotlib.pyplot as plt
import csv
import os

bestand = csv.DictReader(open("desktop.csv"))

d2011 = {}
d2012 = {}
d2013 = {}
d2014 = {}

a = 0
for regel in bestand:
    for k, v in regel.items():
        if k == "Date" or k == "Win7" or k == "WinXP" or k == "WinVista" or k == "OS X" or k == "Win8" or k == "Win8.1" or k == "Linux":
            if a < 8:
                d2011[k] = v
                a += 1
            elif a >= 8 and a < 16:
                d2012[k] = v
                a += 1
            elif a >= 16 and a < 24:
                d2013[k] = v
                a += 1
            elif a >= 24 and a < 32:
                d2014[k] = v
                a += 1
            else:
                break

l2011   = []
l2011_v = []
l2012   = []
l2012_v = []
l2013   = []
l2013_v = []
l2014   = []
l2014_v = []

for k, v in d2011.items():
    if k != "Date" or v != '2011':
        l2011.append(k)
        l2011_v.append(v)

for k, v in d2012.items():
    if k != "Date" or v != '2012':
        l2012.append(k)
        l2012_v.append(v)

for k, v in d2013.items():
    if k != "Date" or v != '2013':
        l2013.append(k)
        l2013_v.append(v)

for k, v in d2014.items():
    if k != "Date" or v != '2014':
        l2014.append(k)
        l2014_v.append(v)

l2011_v = [float(i) for i in l2011_v]
l2012_v = [float(i) for i in l2012_v]
l2013_v = [float(i) for i in l2013_v]
l2014_v = [float(i) for i in l2014_v]

n_groups = 4

l1 = [l2011_v[0], l2012_v[0], l2013_v[0], l2014_v[0]]
l2 = [l2011_v[1], l2012_v[1], l2013_v[1], l2014_v[1]]
l3 = [l2011_v[2], l2012_v[2], l2013_v[2], l2014_v[2]]
l4 = [l2011_v[3], l2012_v[3], l2013_v[3], l2014_v[3]]
l5 = [l2011_v[4], l2012_v[4], l2013_v[4], l2014_v[4]]
l6 = [l2011_v[5], l2012_v[5], l2013_v[5], l2014_v[5]]
l7 = [l2011_v[6], l2012_v[6], l2013_v[6], l2014_v[6]]

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.1

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, l1, bar_width,
                 alpha=opacity,
                 color='red',
                 error_kw=error_config,
                 label=l2011[0])

rects2 = plt.bar(index + bar_width, l2, bar_width,
                 alpha=opacity,
                 color='purple',
                 error_kw=error_config,
                 label=l2011[1])

rects3 = plt.bar(index + bar_width + bar_width, l3, bar_width,
                 alpha=opacity,
                 color='orange',
                 error_kw=error_config,
                 label=l2011[2])

rects4 = plt.bar(index + (bar_width*3), l4, bar_width,
                 alpha=opacity,
                 color='green',
                 error_kw=error_config,
                 label=l2011[3])

rects5 = plt.bar(index + (bar_width*4), l5, bar_width,
                 alpha=opacity,
                 color='blue',
                 error_kw=error_config,
                 label=l2011[4])

rects6 = plt.bar(index + (bar_width*5), l6, bar_width,
                 alpha=opacity,
                 color='brown',
                 error_kw=error_config,
                 label=l2011[5])

rects7 = plt.bar(index + (bar_width*6), l7, bar_width,
                 alpha=opacity,
                 color='black',
                 error_kw=error_config,
                 label=l2011[6])

plt.xlabel('Jaar')
plt.ylabel('Aantal (%)')
plt.title('Top 7 desktop besturingssystemen')
plt.xticks(index + bar_width + bar_width + bar_width + 0.05, (2011, 2012, 2013, 2014))
plt.legend(prop={'size':8})
plt.tight_layout()
plt.show()

filenaam = __file__


os.system("git init")
os.system("git add " + str(filenaam))
os.system("git commit -m 'commit'")
os.system("git pull origin master")
os.system("git remote add origin https://github.com/J4mie1/hello-world.git")
os.system("git push -u origin master")

