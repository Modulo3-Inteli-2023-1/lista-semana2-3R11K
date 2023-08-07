#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def conta_palavras_unicas(text):
    text = text.split()
    checked = []
    count = 0
    for word in text:
        if word not in text or word not in checked:
            count += 1
            checked.append(word)
    return count
# Teste a sua função aqui (caso ache necessário)









