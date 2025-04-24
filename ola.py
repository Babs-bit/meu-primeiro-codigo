#diferentes tipos de variáveis 
idade = 30             #inteiro (int) representa números inteiros, positivos ou negativos, sem parte decimal. 
altura = 1.60           #ponto flutuante (float) representa número com parte decimal (reais) 
nome = "bárbara"        #string (str) representa texto, como palavras ou frases entre aspas simples ou duplas
esta_chovendo = False   #booleano (bool) representa valores lógicos, como verdadeiro ou falso 
hobbies = [ "ler", "malhar", "jogar vídeo game"] #lista (list) armazena múltiplos valores, como uma lista de compras.  
dias = ["segunda", "terça"]  #tupla (tuple) dados ordenados que não podem ser alterados, como dias da semana ou coordenadas
pessoa = {"nome" : "Bárbara", "idade" : 30} #dicionário ( dict) associa informações, como um cadastro 
numeros_unicos = {1, 2, 3} #conjunto vazio (set) coleção de números unicos que elimina duplicatas, verifica pertencimento
#
# O tamanho das variáveis não são fixos, dependem do tipo utilizado; O exemplo tem como referência um PC de 64bits
inteiro = "~28bytes" # 16 + 12
float = "~24bytes" # 16 + 8
string = "~48bytes" # 16 + 33
booleano = "~28bytes" # 16 + 12
lista = "~56bytes" # 16 + 40
tupla = "40bytes" # 16 + 24
dicionário = "~64bytes" # 16 + 48
conjunto vazio = "~72bytes" #16 + 56
#
# 
# Variáveis listadas: int, float, str, bool, list, tuple, dict e set. 
print("idade", idade)
print("altura", altura)
print("nome", nome)
print("esta_chovendo", esta_chovendo)
print("hobbies", hobbies)
print("dias", dias)
print("pessoa", pessoa)
print("numeros_unicos", numeros_unicos)
#
# Diferença entre C e Pyhton 
int idade = 30
float altura = 1.60
char  nome[20] = "bárbara"
