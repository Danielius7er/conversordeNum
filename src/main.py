def bin_to_dec(binario):
    """Converte binário para decimal."""
    if not binario:
        return 0
    if not all(c in '01' for c in binario):
        raise ValueError("O número binário deve conter apenas os dígitos 0 e 1.")
    return int(binario, 2)

def dec_to_bin(decimal):
    """Converte decimal para binário."""
    if decimal < 0:
        raise ValueError("O número decimal deve ser não negativo.")
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario

def oct_to_dec(octal):
    """Converte octal para decimal."""
    if not octal:
        return 0
    if not all(c in '01234567' for c in octal):
        raise ValueError("O número octal deve conter apenas os dígitos 0-7.")
    return int(octal, 8)

def dec_to_oct(decimal):
    """Converte decimal para octal."""
    if decimal < 0:
        raise ValueError("O número decimal deve ser não negativo.")
    if decimal == 0:
        return '0'
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def hex_to_dec(hexadecimal):
    """Converte hexadecimal para decimal."""
    if not hexadecimal:
        return 0
    try:
        return int(hexadecimal, 16)
    except ValueError:
        raise ValueError("O número hexadecimal deve conter apenas dígitos 0-9 e A-F.")

def dec_to_hex(decimal):
    """Converte decimal para hexadecimal."""
    if decimal < 0:
        raise ValueError("O número decimal deve ser não negativo.")
    if decimal == 0:
        return '0'
    hex_chars = '0123456789ABCDEF'
    hexadecimal = ''
    while decimal > 0:
        hexadecimal = hex_chars[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal

def main():
    print("Conversor de Bases Numéricas")
    print("Escolha a base de entrada:")
    print("1. Binário")
    print("2. Decimal")
    print("3. Octal")
    print("4. Hexadecimal")
    
    try:
        entrada_base = int(input("Digite o número da base de entrada: "))
        if entrada_base not in [1, 2, 3, 4]:
            raise ValueError("Base inválida.")
        
        numero = input("Digite o número: ").strip().upper()
        
        print("Escolha a base de saída:")
        print("1. Binário")
        print("2. Decimal")
        print("3. Octal")
        print("4. Hexadecimal")
        
        saida_base = int(input("Digite o número da base de saída: "))
        if saida_base not in [1, 2, 3, 4]:
            raise ValueError("Base inválida.")
        
        # Converter para decimal primeiro
        if entrada_base == 1:
            decimal = bin_to_dec(numero)
        elif entrada_base == 2:
            decimal = int(numero)
        elif entrada_base == 3:
            decimal = oct_to_dec(numero)
        elif entrada_base == 4:
            decimal = hex_to_dec(numero)
        
        # Converter de decimal para a base de saída
        if saida_base == 1:
            resultado = dec_to_bin(decimal)
        elif saida_base == 2:
            resultado = str(decimal)
        elif saida_base == 3:
            resultado = dec_to_oct(decimal)
        elif saida_base == 4:
            resultado = dec_to_hex(decimal)
        
        print(f"O número convertido é: {resultado}")
    
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()