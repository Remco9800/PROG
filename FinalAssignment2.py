#Final Assignment:
#Ik gebruik de gemaakte opdrachten van practice exercise 2 om de github opdrachten van de Final Assignment uit te voeren.
#2_1
Letters =  ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
A = Letters.count("A")
B = Letters.count("B")
C = Letters.count("C")
Voorkomen = (A, B, C)
print(Voorkomen)

#2_2
cijferICOR = 7.5
cijferPROG = 8.0
cijferCSN = 6.5
gemiddelde = (cijferICOR + cijferPROG + cijferCSN) /3
beloning = (cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30)
overzicht = "mijn cijfers gemiddeld een " + str(gemiddelde) + " leveren een beloning van €" + str(beloning) + " op!!!"
print(overzicht)

#2_3
#snap ik helaas niet


#2.4
uurloon = input("wat verdien je per uur?")
uren = input("hoeveel uur heb je gewerkt")
salaris = float(uurloon)*int(uren)
print(salaris)
bericht = str(uren) + " uur werken levert " + str(salaris) + " euro op"
print(bericht)
