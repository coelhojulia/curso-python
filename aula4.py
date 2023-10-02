"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado = tem nome com sinal de igual (=)
Argumento não nomeado + recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição da função
    print(f'{x=} + y={y} z={z}', 'x + y = ', x + y + z)

soma(1, 2, 3) # argumento posicional (não nomeado)
soma(1, 2, z=5) # (argumento nomeado)

print(1, 2, 3, sep='-')

"""
Ou nomeia tudo, ou não nomeia nada.
"""