def biner_ke_desimal(biner):
    return int(biner, 2)
biner = input("Masukkan bilangan biner: ")
desimal = biner_ke_desimal(biner)
print(f"Desimal dari {biner} adalah {desimal}")