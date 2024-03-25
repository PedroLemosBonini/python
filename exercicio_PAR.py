while True:

    numero = int(input("Digite o número: "))

    if numero % 2 == 0 and numero >= 0:
        print('""P-A-R!!!""')
        break
    else:
        print('"Tente outra vez!"')