#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    for i in string1:
        if i not in string2:
            return False
    return True
# Teste a sua função aqui (caso ache necessário)











