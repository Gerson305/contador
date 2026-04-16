import sys
from generator.password_generator import  generate_secure_password

def main():
    if len(sys.argv) < 2:
        print("Para ejecutar Uso: python main.py <longitud>")
        return
    
    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Error: La longitud debe ser un número entero.")
        return
    
    if length < 4:
        print("Error: La longitud debe ser al menos 4.")
        return
    
    password = generate_secure_password(length)
    print(f"Contraseña generada: {password}")

if __name__ == "__main__":
    main()