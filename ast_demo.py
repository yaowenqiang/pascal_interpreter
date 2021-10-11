import ast
import pprint
code = '''
x = [1,2]
print(x)
'''
tree = ast.parse(code)
pprint.pprint(ast.dump(tree))
