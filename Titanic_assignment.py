import pandas as pd
# Importerer statistik modulet som bruges senere.
import statistics as stat
# Importerer collections modulet som bruget til "Counter" og "most_common" senere.
import collections as col 
data = pd.read_csv("titanic.csv")


# Opgave 1 & 2
# Bestemmer hvor meget af dataen man ser og i hvor bredt et format
pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 150)

# Viser hvor mange rækker (første tal) og kolonner (andet tal) der findes i datasættet
print("\n")
print("Datasættet er opbygget af",data.shape,"rækker og kolonner.")
print("\n")

# Viser hvor mange 'celler' der findes i datasættet (rækker x kolonner).
print("Der findes",data.size,"'celler' i datasættet.")
print("\n")

# Viser navnene på kollonerne. 
print("Navnene på diverse kolonner er:",data.columns)
print("\n")

# Viser hvilke datatyper man har at gøre med fra datasættet. I dette tilfælde er det 'int64', 'float64' eller 'object'.
# Forskellen på de tre er at int64 er numeriske tegn, float64 er numeriske tegn med decimaler og object er hvis kolonnen indeholder strings - tekst.  
print("Datatyperne er:\n",data.dtypes)
print("\n")



# Opgave 3
# Her bliver der brugt statistik modulet der blev importeret tidligere for at hurtigt kunne regne gennemsnittet og medianen ud af alder og pris.
gennem_alder = round(stat.mean(data["Age"]),2)
med_alder = stat.median(data["Age"])
gennem_pris = round(stat.mean(data["Fare"]),2)
med_pris = stat.median(data["Fare"])

# Her bliver resultaterne af disse udregninger printet.
print ("Gennemsnitsalderen er:", gennem_alder)
print ("Medianalderen er:", med_alder)
print ("Gennemsnitsprisen er:", gennem_pris)
print ("Medianprisen er:", med_pris)
print("\n")

# Antal mænd og kvinder. f der står lige efter print betyder at man formaterer så man for eksempel kan bruge {male}.
def male_female():
    male=0
    female=0
    for i in data ["Sex"]:
        if i=="male":
            male+=1
        else:
            female+=1
    print(f"Der var {male} mænd og {female} kvinder ombord på Titanic.")
male_female()
print("\n")
  
# Antal overlevende
# Fordi antallet af overlevende er vist i 1 og 0, kan man bruge sum funktionen for at se hvor mange der overlevede.
print("Der var",sum(data["Survived"]),"overlevende i dette datasæt.")

# Man kan også vælge at lave en mere generel funktion hvis antallet af overlevende ikke var vist med 0 og 1... 
def overlevende ():
    resultat = 0
    for i in data["Survived"]:
        if i==1: # Denne skulle blot skiftes ud med det der stod i datasættet. Eksempelvis Y for Yes.
            resultat+=1
    print("Der var", resultat,"overlevende i dette datasæt.")
overlevende()
print("\n")



# Opgave 4
def samme_efternavn():
    efternavne=[]
    for i in data["Name"]:
        uddrag_efternavne = i.split()[-1:]
        for x in uddrag_efternavne:
            efternavne.append(x)
    flest_efternavne=col.Counter(efternavne) # Der bruges "Counter" for at tælle hvor mange gange hvert navn forekommer i listen.
    print("De 8 navne der forekommer hyppigst er:\n",flest_efternavne.most_common(8)) # Der bruges "most_common" for at vise de 8 navne der forekommer hyppigst.
samme_efternavn()
print("\n")



# Opgave 5
# Der laves en funktion for at finde antallet af passagere til hver prisklasse.

first = 0
second = 0
third = 0
for i in data ["Pclass"]:
    if i == 1:
        first += 1
    elif i == 2:
        second += 1
    else:
        third += 1
print(f"Der var {first} passagerer der rejste med første klasse, {second} der rejste med anden klasse og {third} passagerer der rejste med tredje klasse.")
print("\n")

# Der bliver her brugt "groupby" funktionen for at dele dataen op i forhold til "Pclass" og "Survived" kolonnerne. Derefter bliver funktionen "value_counts" brugt for at vise antallet af gange disse værdier forekommer.
print("Her kan man se hvor mange overlevende og omkomne, vist i 1 - overlevende og 0 - omkomne, for hver prisklasse (Pclass):\n\n",data.groupby('Pclass')['Survived'].value_counts())
print("\nSom man kan se, var det prisklasse 3, med 368, der havde flest omkomne.")
