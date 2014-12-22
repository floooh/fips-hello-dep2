"""fips imported code generator for testing"""

Version = 2 

import genutil as util

#-------------------------------------------------------------------------------
def generateHeader(func_name, msg, hdrPath) :
    with open(hdrPath, 'w') as f :
        f.write("// #version:{}#\n".format(Version))
        f.write("extern void {}(void);".format(func_name))

#-------------------------------------------------------------------------------
def generateSource(func_name, msg, srcPath) :
    with open(srcPath, 'w') as f :
        f.write("// #version:{}#\n".format(Version))
        f.write("#include <stdio.h>\n")
        f.write("void {}() {{\n".format(func_name))
        f.write('    printf("{}\\n");\n'.format(msg))
        f.write('}')

#-------------------------------------------------------------------------------
def generate(directory, name, func_name, msg) :
    selfPath = directory + name + '.py'
    hdrPath = directory + name + '.h'
    srcPath = directory + name + '.cc'
    if util.isDirty([selfPath], Version, hdrPath, srcPath) :
        print '## generating {}'.format(hdrPath)        
        generateHeader(func_name, msg, hdrPath)
        print '## generating {}'.format(srcPath)        
        generateSource(func_name, msg, srcPath)
    else :
        print '## nothing to do for {}'.format(selfPath)
