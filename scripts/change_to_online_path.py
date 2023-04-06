import os
import numpy as np
from glob import glob, iglob
import regex as re

#-------------------------------
# Gain .MD list
#--------------------------------
path = '../_posts'

origin_img_source = r'/Users/haochen/Desktop/Python%20Project/chqwer2.github.io/img/Typora/'
# target_img_resource = r'https://chqwer2.github.io/img/Typora/'
target_img_resource = r'https://ik.imagekit.io/haochen/Typora/'


md_list = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.lower().endswith('.md') or f.lower().endswith('.markdown')]

img_list = []

#-------------------------------
# Modify .MD
#--------------------------------
for md in md_list:
    if os.path.isdir(md):
        continue
    if not (md.endswith('md') or md.endswith('markdown')):
        continue

    print("handling ", md)
    md = md.rstrip('markdown').rstrip('.')
    try:
        f = open(md+'.md','r', encoding='utf8')
    except:
        f = open(md + '.markdown', 'r', encoding='utf8')

    data = f.read()
    # Substitute
    new_data = re.sub(origin_img_resource, target_img_resource, data)

    f.close()

    f1 = open(md + '.md', 'w', encoding='utf8')
    f1.write(new_data)

    # Gain IMG list
    # group = re.findall(r"C:(.*)", data)
    # for i, j in enumerate(group):
    #     img_list.append(group[i].split('\\')[-1].rstrip(')'))

    f1.close()

print("successful write MD files...")
