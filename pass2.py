from pass1 import mnttab, pntab, kpdtab, mdttab

macroCall = []  # Storing the macro names
aptab = {}

# Populating the macroCall list with macro names from mnttab
for i in range(len(mnttab)):
    macroCall.append(mnttab[i][0])

with open("input.txt") as f2:
    codelines = f2.readlines()

# Open the output file for writing
with open("sourceProgram.txt", "w") as f3:
    index = 0
    while index < len(codelines):
        # Ignoring the Macro Definition
        if "MACRO" in codelines[index]:
            while "MEND" not in codelines[index]:
                index += 1
            index += 1
        else:        
            # Expansion of Macro code
            line_split = codelines[index].split()
            if line_split and line_split[0] in macroCall:
                serialNo = macroCall.index(line_split[0])
                # setting the values in aptab
                aptabIndex = 1
                while aptabIndex < len(line_split):
                    aptab['P' + str(aptabIndex)] = line_split[aptabIndex].split('=')
                    aptabIndex += 1  
                
                # getting default values from kpdtab
                if len(aptab) != mnttab[serialNo][1]:
                    kptabdict = kpdtab[serialNo]
                    for key, value in kptabdict.items():
                        temp3 = key
                        if temp3 and all(temp3 not in v for v in aptab.values()):
                            aptab['P' + str(aptabIndex)] = [key, value]
                            aptabIndex += 1

                # replacing the values in mdttab and writing the code
                for i in range(len(mdttab[serialNo]) - 1):
                    mdttmp = mdttab[serialNo][i].split()
                    for word in mdttmp:
                        if word in aptab:
                            try:
                                f3.write(aptab[word][1] + ' ')
                            except(IndexError, ValueError):
                                f3.write(aptab[word][0] + ' ') 
                        else:
                            f3.write(word + ' ')
                    f3.write('\n')        
                index += 1    
                print(aptab)
                aptab.clear()  
            else:         
                f3.write(codelines[index])
                index += 1

