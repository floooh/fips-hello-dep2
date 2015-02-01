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
def generate(input, out_src, out_hdr, func_name, msg) :
    if util.isDirty(Version, [input], [out_src, out_hdr]) :
        print '## generating {}'.format(out_hdr)        
        generateHeader(func_name, msg, out_hdr)
        print '## generating {}'.format(out_src)        
        generateSource(func_name, msg, out_src)
    else :
        print '## nothing to do for {}'.format(input)
