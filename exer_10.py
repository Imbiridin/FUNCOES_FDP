def login(usuario, senha):
    
    if usuario == "admin":
        print("Acesso permitido")
    else:
        print("Acesso negado")
    
    if senha == 1234:
        print("Acesso permitido")
    else:
        print("Acesso negado")

login("admin", 1234)