import re

s = "This and that "
m = re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
#print("m ======>>> : ", m)
#print(m(0))
script_file = r'auto_format_disk.sh'
command = '''curl -LJO https://raw.githubusercontent.com/WWBING/python-code/master/mochain/script/{sf} \
    && sh {sf} \
    && rm -rf {sf}'''.format(sf = script_file)
print(s.strip().split(" "))