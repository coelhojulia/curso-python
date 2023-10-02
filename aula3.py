"""
Funções (def) em Python
São trechos de códigos usados para replicar
determinada ação ao longo do código.
Podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

"""def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)"""

def saudacao(nome='Sem Nome'):
    print(f'Ola, {nome}!')

saudacao('Julia')
saudacao('Maria')
saudacao('João')