
def encode(bits_pre):
    encoded_result = []
    dictionary = {1: "1110", 0: "1000", "preamble": '10000000000000000000000000000000'}

    encoding = {key: dictionary[key] for key in list(dictionary)[:2]}
    preamble = {key: dictionary[key] for key in list(dictionary)[2:]}

    for bit in bits_pre:
        encoded_result.extend([int(char) for char in encoding[bit]])

    #Preambule&mode codification
    preamble = preamble['preamble']
    mode = [0,0,1,0]  # unlock'
    mode_result = []
    for bit in mode:
        mode_result.extend([int(char) for char in encoding[bit]])

    bits = [int(char) for char in preamble] + encoded_result + mode_result

    return bits

def num2bits(num):
    binary_str = bin(num)[2:]
    bits_list = ','.join(binary_str)
    bits_list = [int(bit) for bit in bits_list.split(',')]
    signal = encode(bits_list)
    return signal

def bits2num(bits):
    binary_list = [int(bit) for bit in bits.split(',')]
    number = int(''.join(map(str, binary_list)), 2)
    return number

