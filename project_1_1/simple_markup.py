import sys, re
from util import *

# print  >***.html
print('<html><head><title>...</title><body>')
title = True
# sys.stdin
for block in blocks(sys.stdin):
    # 正则表达式
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')