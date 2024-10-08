"""
# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys

platform = 'A MINHA'
print(sys.platform)
print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
from sys import exit, platform

print(platform)

# alias 1 - import nome_modulo as apelido
import sys as s

sys = 'alguma coisa'
print(s.platform)
print(sys)


# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex
from sys import platform as pf

print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import exit, platform

print(platform)
exit()
"""

"""
# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import sys
import app_modul


print('Este módulo se chama', __name__, 'Executado aqui')
print('Pastas do python abaixo:')
print(*sys.path, sep='\n')
"""

""""""
#Como importar coisas do seu próprio módulo
#(Ponto de vista do __main__)
import app_modul
from app_modul import variavel_modul
#print('Este módulo se chama', __name__, 'Executado aqui')
print(app_modul.variavel_modul) #Com import
print(variavel_modul) #Importando só uma coisa
