def inverter_string(string):
    # armazena a string invertida
    string_invertida = ""

    for i in range(len(string) - 1, -1, -1):
        
        string_invertida += string[i]
        
    return string_invertida

# Execução do código
string_original = "Nada lhe pertence mais que seus sonhos"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)