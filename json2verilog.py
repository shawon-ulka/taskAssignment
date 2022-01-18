import json

with open("portData","r") as f:
    jsonDict=json.load(f)
f.close()
def sizeFormat(size):
    if size==1:
        return ""
    strSize=f"[{size-1}:0]"
    return strSize
with open("output.sv","w") as outputFile:
    outputFile.writelines("// Code Generated from Excel\n")
    outputFile.writelines(f"`timescale {jsonDict['timescale']}\n\n")
    outputFile.writelines(f"module {jsonDict['module name']} (\n")
    for key, value in jsonDict["allPortInfo"].items():
        portName=key
        portDirection=value["direction"]
        size=sizeFormat(value["size"])
        type=value["type"]
        outputFile.writelines(f"\t{portDirection}\t{type}\t{size}\t{portName}\n")
    outputFile.writelines(");\n\n")
    outputFile.writelines("endmodule")