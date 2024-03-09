def inverter_string(s):
    # Converte a string para uma lista de caracteres
    caracteres = list(s)
    
    # Obtém o comprimento da string
    tamanho = len(caracteres)
    
    # Inverte os caracteres usando um loop
    for i in range(tamanho // 2):
        # Troca os caracteres nas posições i e tamanho - i - 1
        caracteres[i], caracteres[tamanho - i - 1] = caracteres[tamanho - i - 1], caracteres[i]
    
    # Converte a lista de caracteres de volta para uma string
    string_invertida = ''.join(caracteres)
    
    return string_invertida

# Exemplo de uso:
entrada = input("Digite uma string: ")
resultado = inverter_string(entrada)
print("String invertida:", resultado)
