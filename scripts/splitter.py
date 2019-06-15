def read():
    import os
    import sys
    import re

    arguments = sys.argv
    dir = "."

    if not arguments[1]:
        sys.exit('Error in path')
    else:
        dir = arguments[1]

    resultDir = os.getcwd()+"/../results"
    if not os.path.isdir(resultDir):
        os.mkdir(resultDir)

    counter = 0

    for f in os.listdir(dir):
        file = open(os.path.join(dir, f), 'r')
        tokens = f.split(".")
        group = tokens[3]
        flag = 0
        count = 0

        line = file.readline()
        while line != "":
            line = line.rstrip("\n")
            if line.find("num_ind") != -1:
                line = re.sub("[0-9]+\s+", "", line)
                out_file = open(os.path.join(resultDir, str('parity.group('+str(group)+').generation('+str(count)+').csv')), 'w')
                out_file.write(line+"\n")
                flag = 1
                count += 1
                            
            line = file.readline()            
              
            if flag == 1:
                out_file.write(line)
            
            tokens = line.split(";")
            if tokens[0] == '1023':
                out_file.close()
                flag = 0                


read()
