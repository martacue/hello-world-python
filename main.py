import sys
import json

def main():
    # argumentos de la línea de comandos (excepto el primer argumento, que es el nombre del script)
    args = sys.argv[1:]

    # Verifica si se proporcionaron argumentos
    if not args:
        print("Proporciona un JSON como argumento.")
        return

    # El primer argumento es tratado como el JSON
    json_string = args[0]

    try:
        # analizar el JSON
        data = json.loads(json_string)

        # Imprime el contenido del JSON
        print("Contenido del JSON:")
        print(json.dumps(data, indent=2))

    except json.JSONDecodeError as e:
        print(f"Error al decodificar el JSON: {str(e)}")

if __name__ == "__main__":
    main()

