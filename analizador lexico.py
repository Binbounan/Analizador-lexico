import re

# Definición de tokens
TOKEN_REGEX = [
    (r'\bif\b|\bwhile\b|\breturn\b|\belse\b|\bint\b|\bfloat\b', 'PALABRA_RESERVADA'),
    (r'[a-zA-Z][a-zA-Z0-9]*', 'IDENTIFICADOR'),
    (r'\d+\.\d+', 'REAL'),
    (r'\d+', 'ENTERO'),
    (r'\+|\-', 'OPERADOR_ADICION'),
    (r'\*|/', 'OPERADOR_MULTIPLICACION'),
    (r'=', 'OPERADOR_ASIGNACION'),
    (r'<=|>=|!=|==|<|>', 'OPERADOR_RELACIONAL'),
    (r'&&', 'OPERADOR_AND'),
    (r'\|\|', 'OPERADOR_OR'),
    (r'!', 'OPERADOR_NOT'),
    (r'\(|\)', 'PARENTESIS'),
    (r'\{|\}', 'LLAVE'),
    (r';', 'PUNTO_Y_COMA'),
    (r'\s+', None)  # Ignorar espacios en blanco
]

def analizador_lexico(codigo):
    tokens = []
    while codigo:
        for patron, tipo in TOKEN_REGEX:
            regex = re.match(patron, codigo)
            if regex:
                if tipo:
                    tokens.append((regex.group(), tipo))
                codigo = codigo[len(regex.group()):]
                break
        else:
            raise ValueError(f'Error léxico: {codigo}')
    return tokens

# Bucle para seguir ingresando código
while True:
    codigo_prueba = input("Ingrese el código a analizar (o 'salir' para terminar): ")
    if codigo_prueba.lower() == 'salir':
        print("Saliendo...")
        break
    try:
        tokens = analizador_lexico(codigo_prueba)
        for token in tokens:
            print(token)
    except ValueError as e:
        print(e)
