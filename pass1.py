mnttab = []
pntab = []
kpdtab = []
mdttab = []

def macroProcessor(macrolines, start_index):
    mntinfo = []
    # reading first macro line to get info about macro
    mntLine = macrolines[start_index].replace("\n", '').replace("=", ' ').split()
    
    # storing the name of macro in mnt
    mntinfo.append(mntLine[0])
    
    # storing the name of parameters in pntab
    pntinfo = {}
    for i in range(len(mntLine)):
        if "&" in mntLine[i]:
            pntinfo[mntLine[i]] = "P" + str(i)
    
    # storing number of parameters in mnttab
    mntinfo.append(len(pntinfo))
    
    # storing the values in kpdtab
    keyDict = {}
    temp = macrolines[start_index].split()
    for i in range(len(temp)):
        if "=" in temp[i]:
            temp2 = temp[i].split('=')
            try:
               keyDict[temp2[0]] = temp2[1]
            except (IndexError, ValueError):
               keyDict[temp2[0]] = "notset"   
    kpdtab.append(keyDict)
    
    # storing kpdtab pointer in mnttab
    mntinfo.append(len(kpdtab))
    
    # putting the values in actual pntab and mnttab
    mnttab.append(mntinfo)
    pntab.append(pntinfo)
    

    # mdttab processing
    mdtinfo = []
    for i in range(start_index + 1, len(macrolines)):
        mdtline = ""
        if "MEND" in macrolines[i]:
            mdtline = "MEND"
            mdtinfo.append(mdtline)
            mdttab.append(mdtinfo) 
            return i  # Return the index of the line after MEND
        else:
            macrolineArray = macrolines[i].replace(',', '').split()
            for j in range(len(macrolineArray)):
                if macrolineArray[j] in pntinfo:
                    mdtline += pntinfo[macrolineArray[j]] + " "
                else:
                    mdtline += macrolineArray[j] + " "
            mdtinfo.append(mdtline)       
    
    return len(macrolines)  # If no MEND found, return the end of the list


if __name__ == "__main__":
    with open("input.txt") as f1:
        macrolines = f1.readlines()

    index = 0
    while index < len(macrolines):
        line = macrolines[index]
        if "MACRO" in line:
            index = macroProcessor(macrolines, index + 1)  # Process macro and get the next index
        else:
            index += 1  # Move to the next line

    print(mnttab)
    print(pntab)
    print(kpdtab)
    print(mdttab)
