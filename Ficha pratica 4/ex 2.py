#variavel somatório
somatorio = 0

#print numeros impares de 11 a 51
for i in range(11, 52, 2):
    print(i)
    somatorio += i  # somatorio = somatorio + i

#somatório de todos os numeros
print("Somatório:", somatorio)