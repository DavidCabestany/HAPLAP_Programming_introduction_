import os
fout = open("functions.py","w")
init = open("__init__.py","w")
for fn in os.listdir("."):
    if fn.startswith("ex") and fn.endswith(".py"):
        func = False
        for line in open(fn):
            if line.strip() == "":
                continue
            if (func and (line.startswith(" ") or line.startswith("\t"))) or line.startswith("import ") or line.startswith("from "):
                fout.write(line)
            elif line.startswith("def "):
                func = True
                fout.write(line)
            elif func and not line.startswith(" ") and not line.startswith("\t"):
                func = False
                fout.write("\n")
        fout.write("\n")
fout.close()
init.close()