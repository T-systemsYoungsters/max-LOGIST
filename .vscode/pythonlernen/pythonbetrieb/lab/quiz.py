# Quiztime
i=0
print("Im folgenden Quiz werden dir 5 Fragen gestellt, die du richtigt beantworten musst, um zu gewinnen.")
question1=int(input("Frage 1: Was ergibt 12*12? "))
if question1==144:
    i=1
    print("Das ist richtig.")
    question2=input("Frage 2: Wie lautet der Nachname des amerikanische Präsidenten? ")
    if question2=="Biden" or question2=="biden":
        i=2
        print("Das ist richtig.")
        question3=int(input("Frage 3: In welchem Jahr hat Kolumbus, Amerika entdeckt? "))
        if question3==1492:
            i=3
            print("Das ist richtig.")
            question4=input("Frage 4: Wie lautet der Vorname des besten Freundes von Harry Potter? ")
            if question4=="Ron" or question4=="ron":
                i=4
                print("Das ist richtig.")
                print("Frage 5: Wie hoch ist der Mount Everest?")
                print("A 7342 \nB 8213 \nC 8848")
                question5=input("Wählen sie die richtige Antwortmöglichkeit: ")
                if question5 =="C" or question5=="c":
                    print("Sie haben alle Fragen richtig beantwortet und haben gewonnen.")
                else:
                    print("Sie haben leider verloren.")
            else:
                print("Sie haben leider verloren.")
        else:
            print("Sie haben leider verloren.")
    else:
        print("Sie haben leider verloren.")
else:
    print("Sie haben leider verloren.")
p=i/5*100
print("Sie haben",p,"Prozent der Fragen richtig beantwortet")