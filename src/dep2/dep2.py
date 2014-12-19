"""code generator test"""
import hello_generator as gen

def generate(directory, name) :
    gen.generate(directory, name, 'print_dep2', 'Hello from dep2!')


