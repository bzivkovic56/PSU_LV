# Zadatak1
# def total_euro(radni,sat):
#     return radni*sat

# radni_sati=int(input("Unesite broj radnih sati: \n"))
# satnica=float(input("Unesite vasu satnicu: \n"))
# ukupno=total_euro(radni_sati,satnica)
# print(ukupno)


# Zadatak2
# try:
#     ocjena=float(input("Unesite ocijenu: \n"))
#     if ocjena>=0.0 or ocjena<=1.0:
#         if(ocjena>=1.0):
#             print("Ponovite unos")
#         elif(ocjena>=0.9):
#             print("A")
#         elif(ocjena>=0.8):
#             print("B")
#         elif(ocjena>=0.7):
#             print("C")
#         elif(ocjena>=0.6):
#             print("D")
#         else:
#             print("F")
            


# except:
#     print("Upisite valjan uvjet")

# Zadatak3
# brojevi=[]
# brojac=0
# try:
#     while True:
#         broj=int(input("Unesite broj u listu: \n"))
#         if broj=="Done":
#             break
#         else:
#             brojevi.append(broj)
#             brojac+=1


# except:
#     print("Unesite valjan unos\n")

# print("Korisnik je unio ",brojac," brojeva")
# print("Srednja vrijednost: ",sum(brojevi)/len(brojevi))
# print("Minimalna vrijednost: ",min(brojevi))
# print("Maksimalna vrijednost: ",max(brojevi))
# brojevi.sort()
# print(brojevi)

# #Zadatak4
# spam_counter = 0
# sum = 0.0

# unos = input("unesite ime tekstualne datoteke \n")
# datoteka = 'C:\\Users\\student\\Desktop\\PSU\\'+unos+'.txt'
# try:
#   dat = open(datoteka, 'r')
# except:
#     print("Datoteka ne postoji")

# for line in dat:
#    line = line.split()
#    if("X-DSPAM-Confidence:" in line):
#       spam_counter += 1
#       sum += float(line[1])


# print("Srednja vrijednost pouzdanosti je : ", sum/spam_counter)