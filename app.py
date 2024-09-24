import re
from collections import Counter
from tabulate import tabulate # Biblioteca para organizar em tabela

# Função para normalizar e contar as palavras no texto
def contar_palavras(texto):
    # Remove pontuação e converte tudo para minúsculas
    palavras = re.findall(r'\b\w+\b', texto.lower())
    
    # Conta a frequência de cada palavra
    contador = Counter(palavras)
    
    return contador

# Função para exibir as palavras mais frequentes 
def exibir_palavras_frequentes(contador):
    # Ordena as palavras pela contagem
    palavras_ordenadas = sorted(contador.items(), key=lambda item: item[1])
    
    # Prepara a tabela com as palavras e suas frequências
    tabela = [[palavra, frequencia] for palavra, frequencia in palavras_ordenadas]
    
    # Exibe a tabela usando tabulate
    print(tabulate(tabela, headers=["Palavra", "Frequência"], tablefmt="grid"))

# Função principal
def main():
    # Recebe o texto do usuário
    texto = input("Digite o texto para análise: ")
    
    # Conta a frequência das palavras
    contador = contar_palavras(texto)
    
    # Exibe as palavras e suas frequências
    exibir_palavras_frequentes(contador)

if __name__ == "__main__":
    main()
