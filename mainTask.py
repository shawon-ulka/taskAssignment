import json
from textwrap import indent
from utils import readFile, bitAddressSize

lines=readFile("task.sv")
info={
    "module name":"",
    "timescale":""
}
port=["input","output","inout"]
allPortInfo={}
for line in lines:
    modifiedLine=line.strip()
    if modifiedLine.startswith("module"):
        splitedLine=modifiedLine.split()
        info["module name"]=splitedLine[1]
        continue
    if modifiedLine.startswith("`timescale"):
        splitedLine=modifiedLine.split()
        info["timescale"]=splitedLine[1]
        continue
    splitedLine=modifiedLine.split()
    if len(splitedLine) and splitedLine[0] in port:
        port_dict={}
        port_dict["direction"]=splitedLine[0]
        port_dict["size"]=1
        if len(splitedLine)>=4:
            port_dict["type"]=splitedLine[1]
            if splitedLine[2].startswith("[") and splitedLine[2].endswith("]"):
                size=bitAddressSize(splitedLine[2])
                port_dict["size"]=size
            name=splitedLine[3].replace(',','')
            port_dict["name"]=name
        elif len(splitedLine)==2:
            port_dict["type"]="wire"
            name=splitedLine[1].replace(',','')
            port_dict["name"]=name
        elif len(splitedLine)==3:
            if splitedLine[1].startswith("[") and splitedLine[1].endswith("]"):
                port_dict["type"]="wire"
                size=bitAddressSize(splitedLine[1])
                port_dict["size"]=size
            else:
                port_dict["type"]=splitedLine[1]
            name=splitedLine[2].replace(',','')
            port_dict["name"]=name
        portDetails={"direction":port_dict["direction"],"type":port_dict["type"],"size":port_dict["size"]}
        allPortInfo[port_dict["name"]]=portDetails

info["allPortInfo"]=allPortInfo


portData=json.dumps(info, indent=4)
with open ("portData","w") as f:
    f.write(portData)