import ast
import dis
code = '''
x = [1,2]
print(x)
'''
dis.dis(code)
