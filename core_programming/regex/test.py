import re

s = "This and that "
m = re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print("m ======>>> : ", m)
print(m(0))