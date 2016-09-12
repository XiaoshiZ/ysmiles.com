from time import strftime

title = input("title: ")
subtitle = input("subtitle: ")
author = input("author: ") or 'YS'
date = strftime("%Y-%m-%d %H:%M") 
headerimg = input("header-img: ")
catalog = input("catalog: ") or 'true'
headermask = input("herader-mask: ")
tags = input("tags: ") or 'unclassified'
tags = tags.split()

filename =  '_posts/' + date[:10] + '-' + '-'.join(title.split()) + '.md'
if headerimg != '':
    imgname = '"img/' + headerimg + '"'
else:
    imgname = ''

with open(filename, 'w') as myfile:
    myfile.write('---\n')
    myfile.write('layout:     post\n')
    myfile.write('title:      "' + title + '"\n')
    myfile.write('subtitle:   "' + subtitle + '"\n')
    myfile.write('author:     "' + author + '"\n')
    myfile.write('date:       ' + date + '\n')
    myfile.write('header-img: ' + imgname + '\n')
    myfile.write('catalog:    ' + catalog + '\n')
    myfile.write('header-mask: ' + headermask + '\n')
    myfile.write('tags:\n')
    for tag in tags:
        myfile.write('    - ' + tag + '\n')
    myfile.write('---\n')
