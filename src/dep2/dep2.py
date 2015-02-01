"""code generator test"""
import hello_generator as gen

def generate(input, out_src, out_hdr) :
    gen.generate(input, out_src, out_hdr, 'print_dep2', 'Hello from dep2!')


