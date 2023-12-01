def xor_biner(biner1, biner2):
    num1 = int(biner1, 2)
    num2 = int(biner2, 2)
    result = num1 ^ num2
    result_biner = bin(result)[2:]
    return result_biner

biner1 = "1010010"
biner2 = "1000011"

hasil_xor = xor_biner(biner1, biner2)
print(f"hasil XOR dari {biner1} dan {biner2} adalah {hasil_xor}")