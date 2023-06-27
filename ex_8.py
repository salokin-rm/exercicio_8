"""
Nome: Equação Linear
Descrição: Este programa resolve uma equação linear da forma a*x = b
Autor: Nikolas
Data: 26/06/2023
Versão: 0.0.1
"""

print("Este programa resolve uma equação linear da forma a*x = b")

### Atribuição de variáveis e entrada de dados

a = float(input(f"\nDigite o termo \"a\" da equação:"))
b = float(input(f"\nDigite o termo \"b\" da equação:"))

### Processamento de dados

x = b/a

### Saída de dados

print("\nO valor de x é igual a:",x,)