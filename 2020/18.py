import ast
import fileinput

data = [line.rstrip() for line in fileinput.input()]

p1 = 0

for l in data:
    tree = ast.parse(l.replace('*', '-'))
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp):
            if isinstance(n.op, ast.Sub):
                n.op = ast.Mult()

    p1 += eval(compile(ast.Expression(tree.body[0].value) , '_', 'eval'))

print(p1)


p2 = 0

for l in data:
    tree = ast.parse(l.translate(str.maketrans({'*': '+', '+': '*'})))
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp):
            if isinstance(n.op, ast.Mult):
                n.op = ast.Add()
            elif isinstance(n.op, ast.Add):
                n.op = ast.Mult()

    p2 += eval(compile(ast.Expression(tree.body[0].value) , '_', 'eval'))

print(p2)
