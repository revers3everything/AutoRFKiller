def transformar_bits(bits):
    # Diccionario de transformación
    transformacion = {'1': '1110', '0': '1000'}
    
    # Transformar cada bit en la cadena de entrada y unir con comas
    bits_transformados = ','.join(','.join(transformacion[bit]) for bit in bits)
    
    return bits_transformados

# Ejemplo de uso
entrada = '010100001011110100010010'
salida = transformar_bits(entrada)
print("1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"+salida)  # Salida esperada: 111011101000
