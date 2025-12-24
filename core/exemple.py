errors = {
            "error1": "Veuillez remplir tous les champs !",
            "error2" : "erreur 2 merci"
        }
def simplice():
    while True:
        i = int(input("Fait un choix  ex: (10, 20, 0)"))
        if i == 10:
            error = errors["error1"]
            print(error)
        elif i ==20:
            error = errors["error2"]
            print(error)  
        elif i == 0:
            print("Fonction break ok ?")
            break
            
print(simplice())