"""
#Recarregando módulos, importlib e singleton
import importlib

import app2_m
print(app2_m)

for i in range(10):
    importlib.reload(app2_m)
    print(i)
print('Fim')
"""