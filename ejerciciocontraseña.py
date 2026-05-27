#magina que estás creando el sistema de registro para una aplicación y quieres que las contraseñas de los usuarios sean un poco más seguras.
#El objetivo: Crea una variable llamada contrasena y asígnale el texto que tú quieras. Luego, el programa debe imprimir True si la contraseña contiene un carácter especial (por ejemplo, un asterisco *) y False si no lo tiene.

#Se crea la variable = input(el usuario escribe la contraseña)
Contraseña=input("Contraseña")
#El caracter especial que busca la maquina
Caracter_especial=( "*" )
#Busca si este caracter está en la contraseña
print(Caracter_especial in Contraseña) 

