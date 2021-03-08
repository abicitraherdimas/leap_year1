#pseudo code
# if input tahun % 400 = 0 maka tahun kabisat
# if input tahun % 100 = bukan tahun kabisat
# if input tahun % 4 = tahun kabisat

try:
    input_tahun = int(input("Masukan tahun : "))
    if input_tahun % 4 == 0:
        if input_tahun % 100 == 0:
            if input_tahun % 400 == 0:
                print("Tahun Kabisat")
            else:
                print("Bukan Tahun Kabisat")
        else:
            print("Tahun Kabisat")
    else:
        print("Bukan Tahun Kabisat")
except:
    print("Input tidak dapat menerima string")