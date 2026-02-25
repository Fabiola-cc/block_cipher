def apply_padding(input_string, block_size):
    """
    Aplica padding PKCS#7 a la cadena de entrada.
    """
    # Calcular el número de bytes de padding necesarios
    padding_length = block_size - (len(input_string) % block_size)
    if padding_length == 0:
        padding_length = block_size  # Si ya es múltiplo, agregar un bloque completo de padding
    # Crear el padding
    padding = bytes([padding_length] * padding_length)
    # Devolver la cadena original con el padding añadido
    return input_string + padding
    

def remove_padding(padded_string, block_size):
    """
    Elimina el padding PKCS#7 de la cadena de entrada.
    """
    # Obtener el valor del último byte para determinar la longitud del padding
    padding_length = padded_string[-1]

    # Verificar que el padding sea válido
    if padding_length < 1 or padding_length > block_size:
        raise ValueError("Padding inválido")
    # Verificar que los bytes de padding sean correctos
    if padded_string[-padding_length:] != bytes([padding_length] * padding_length):
        raise ValueError("Padding inválido")
    
    # Devolver la cadena original sin el padding
    return padded_string[:-padding_length]
    