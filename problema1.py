## 1.Scrieti o functie care citeste de la tastatura nume, prenume, varsta  de n ori (n citit de la tastatura) si salveaza informatiile intr-un fisier json.

# import json

# def colectare_date():
#     n = int(input("Introdu numarul de persoane: "))

#     date_persoane = []
    
#     for i in range(n):
#         print(f"Persoana {i+1}:")
#         nume = input("Introdu numele: ")
#         prenume = input("Introdu prenumele: ")
#         varsta = int(input("Introdu varsta: "))
        
#         persoana = {
#             "nume": nume,
#             "prenume": prenume,
#             "varsta": varsta
#         }
        
#         date_persoane.append(persoana)
    
#     with open("date_persoane.json", "w") as fisier:
#         json.dump(date_persoane, fisier, indent=4)
    
#     print("Datele au fost salvate in fisierul 'date_persoane.json'.")

# colectare_date()


## 2.Scrieti o functie care citeste un fisier json de tipul celui de la problema 1 si scrie informatiile in format csv

# import csv

# def json_csv(json_file, csv_file):
  
#     with open(json_file, 'r') as f:
#         data = json.load(f)
    
#     with open(csv_file, 'w', newline='') as f:
    
#         fieldnames = data[0].keys()
        
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
        
#         writer.writeheader()
        
#         for row in data:
#             writer.writerow(row)
    
#     print(f"Datele au fost salvate in fisierul '{csv_file}'.")

# json_csv('date_persoane.json', 'date_persoane.csv')

## 3.Scrieti o functie care numara cate persoane sunt inregistrate in fisierul csv


# def numara_persoane_csv(csv_file):
#     with open(csv_file, 'r') as f:
#         reader = csv.reader(f)
#         next(reader)
#         numar_persoane = sum(1 for row in reader)
    
#     return numar_persoane

# csv_file = 'date_persoane.csv'
# numar_persoane = numara_persoane_csv(csv_file)
# print(f"Numărul de persoane înregistrate în fișierul '{csv_file}' este: {numar_persoane}")

## 4.Scrieti o functie care identifica pe baza informatiilor din fisierul json generat la problema 1, persoana cea mai tanara din lista


# def persoana_tanara(json_file):
 
#     with open(json_file, 'r') as f:
#         data = json.load(f)
    
#     if not isinstance(data, list):
#         print("Formatul fișierului JSON nu este corect.")
#         return
    
#     cea_mai_tanara = min(data, key=lambda persoana: persoana['varsta'])
    
#     return cea_mai_tanara

# json_file = 'date_persoane.json'
# tanara_persoana = persoana_tanara(json_file)

# if tanara_persoana:
#     print(f"Cea mai tânără persoană este {tanara_persoana['nume']} {tanara_persoana['prenume']} cu vârsta de {tanara_persoana['varsta']} ani.")
