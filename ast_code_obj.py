import ast
import pprint
code = '''
x = [1,2]
print(x)
'''
tree = ast.parse(code)
code_obj = compile(tree, 'myfile.py', 'exec')
exec(code_obj)
print(code_obj.co_filename)
