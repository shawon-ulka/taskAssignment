def readFile(filePath):
    with open(filePath,"r") as f:
        lines=f.readlines()
    return lines

def bitAddressSize(bitAddress):
    size=1
    for index,address in enumerate(bitAddress):
        if index==1:
            size+=int(address)
    return size