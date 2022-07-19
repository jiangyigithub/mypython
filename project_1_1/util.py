def lines(file):
    for line in file:yield line
    #生成器怎么用
    yield '\n'

def blocks(file):
    block=[]
    # 字符串操作和IO读写
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block= []