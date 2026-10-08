# Descripción: Captura datos de usuario, aplica formateo de 
# texto y realiza el cálculo de IMC validado.

# --- BLOQUE 1: Captura y formateo de nombres ---
nombre = input("Ingresa tu nombre: ").strip().title()
apellido_paterno = input("Ingresa tu apellido paterno: ").strip().title()
apellido_materno = input("Ingresa tu apellido materno: ").strip().title()

# Validar que no dejen campos de texto vacíos
while not nombre or not apellido_paterno or not apellido_materno:
    print("\n[ERROR] Los campos de nombre y apellidos no pueden estar vacíos.")
    nombre = input("Ingresa tu nombre:").strip().title()
    apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
    apellido_materno = input("Ingresa tu apellido materno: ").strip()

# Formatear cada texto con la primera letra en mayúscula (.title())
nombre_completo = f"{nombre.title()} {apellido_paterno.title()} {apellido_materno.title()}"

# Prueba de salida para el Bloque 1
print(f"\nNombre formateado correctamente: {nombre_completo}")