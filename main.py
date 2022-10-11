def demandeNombre():  # demande nombre
    note = input("")
    try:
        noteInt = int(note)
    except  ValueError:
        print("erreur Vous devez entre un nombre")
        return demandeNombre()
    return noteInt

print("Entre un nombre : ")
nombre1 = demandeNombre()

print("entre un operateur aux choix (*,+,-,/ )")
operator = input("reponse : ")

print("Entre un autre nombre :  ")
nombre2 = demandeNombre()

match(operator):
    case "+":
        print(f"somme de {nombre1} {operator} {nombre2} = {sum(nombre1,nombre2)} ")
    case "-":
        print(f"la soustration de {nombre1} {operator} {nombre2} = {nombre1 - nombre2} ")
    case "*":
            print(f"la multiplication  de {nombre1} {operator} {nombre2} = {nombre1 * nombre2} ")
    case "/":
        print(f"la division  de {nombre1} {operator} {nombre2} = {nombre1 / nombre2} ")
    case default:
        print("operateur inconnue ")