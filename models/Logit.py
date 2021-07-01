import os

def logit(st):
    f = open('/Users/anthonyarmour/VS_Code_Folders/HackSprint/log_file.txt', "a")
    f.write("\n" + st + "\n")
    f.close()