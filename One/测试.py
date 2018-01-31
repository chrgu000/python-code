import sys

lista = ["funca","funcb","funcc"]

FUNC_TEMPLATE = "def {func}(): print(\"I'm Han!!\")"

for fn in lista:
    exec(FUNC_TEMPLATE.format(func=fn))

local_vars = dict(locals().items())

funcs = [local_vars[f] for f in lista]

funcs[0]()
funca()


