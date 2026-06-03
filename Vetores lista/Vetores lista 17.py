"""Faça uma função que recebe uma lista de números e retorna uma nova lista com o fatorial de cada número"""


def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1

    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial = fatorial * i

    return fatorial


def lista_fatoriais(lista_original):
    lista_resultados = []
    for num in lista_original:
        resultado = calcular_fatorial(num)
        lista_resultados.append(resultado)
    return lista_resultados


meus_numeros = []

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número para a lista: "))
    meus_numeros.append(num)

resultado_final = lista_fatoriais(meus_numeros)

print(f"Lista do usuário: {meus_numeros}")
print(f"Lista com os fatoriais: {resultado_final}")