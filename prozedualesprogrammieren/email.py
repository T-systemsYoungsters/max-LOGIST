mail=input("bitte geben sie ihre Email-Adresse an:")
a=mail.find("@")
b=mail.count("@")
c=mail.find(".")
if a>-1 and b==1 and c>a+1:
    print("richtige mail")
else:
    print("falsche mail")