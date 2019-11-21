from collections import OrderedDict
# Создаем словарь Ordered
from typing import Dict

# это алиас для типа Dict
dic_type = Dict[str, int]

# это переменная типа dict_type
dic_t: dic_type = {}

dic = {'a': 14, 'd': 152, 'g': 162, 'j': 612, 'l': 212, 'w': 912, 'r': 112, 'c': 412}

for key in dic.keys():
    key_t = key
    dic_t[key_t] = dic[key]


import re

LOG_ENTRY_RE = '\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6}\]\sN?OK'
string_for_re = '[2018-05-14 19:38:25.873687] NOK'

res = re.findall(LOG_ENTRY_RE, string_for_re)
print(res)

