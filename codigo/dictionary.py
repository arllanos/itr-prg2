socios = [
    {
        "nombre": "Juan",
        "apellido": "Perez",
        "edad": 25,
        "email": "juan@gmail.com",
    },
    {
        "nombre": "Maria",
        "apellido": "Gonzalez",
        "edad": 30,
        "email": "maria@gmail.com"
    },
    {
        "nombre": "Pedro",
        "apellido": "Gomez",
        "edad": 35,
        "email": "pedro@gmail.com"
    }
]

# crear un lista subtreinta_emails con los emails y edad de los socios a partir de los 30 años
# subtreinta_emails = []
# for socio in socios:
#     if socio["edad"] >= 30:
#         subtreinta_emails.append() 

subtreinta_emails = [{"edad": socio["edad"], "email": socio ["email"]} for socio in socios if socio["edad"] >= 30]
print(subtreinta_emails)
