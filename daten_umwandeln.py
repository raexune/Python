#String --> Ganzzahl
a = "5"
b = "6"

print(int(a) + int(b))

#String --> Kommazahl
a = "5.5"
b = "6.5"

print(float(a) + float(b))

#Zahl --> String
a = 5
b = 6

print(str(a) + str(b))

age = 34

print("Ich bin " + str(age) + " Jahre alt.")

#Liste --> String
students = ["Max", "Monika", "Erik", "Franziska"]
print(", ".join(students))

students_as_string = ", ".join(students)
print("An unserer Uni studieren: " + students_as_string)

#String --> Liste
i = "Max, Monika, Erik, Franziska"
print(i.split(", "))

#Satzlänge berechnen
s = "Ich bin ein Satz mit vielen Wörtern."
print(len(s.split(" ")))

