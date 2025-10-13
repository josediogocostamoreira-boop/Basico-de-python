totalSegundosAlbum = 0
minutosLidos = 0
segundosLidos = 0

# Música 1
minutosLidos = int(input("Minutos da 1º música: "))
segundosLidos = int(input("Segundos da 1º música: "))
totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

# Música 2
minutosLidos = int(input("Minutos da 2º música: "))
segundosLidos = int(input("Segundos da 2º música: "))
totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

# Música 3
minutosLidos = int(input("Minutos da 3º música: "))
segundosLidos = int(input("Segundos da 3º música: "))
totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

# Música 4
minutosLidos = int(input("Minutos da 4º música: "))
segundosLidos = int(input("Segundos da 4º música: "))
totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

# Música 5
minutosLidos = int(input("Minutos da 5º música: "))
segundosLidos = int(input("Segundos da 5º música: "))
totalSegundosAlbum = totalSegundosAlbum + (minutosLidos * 60) + segundosLidos

# print("Total Segundos Álbum:",totalSegundosAlbum)

horas = totalSegundosAlbum // 3600

minutos = (totalSegundosAlbum // 60) - (horas * 60)

segundos = totalSegundosAlbum - (horas*3600) - (minutos*60)

print(horas, ":", minutos, ":", segundos)