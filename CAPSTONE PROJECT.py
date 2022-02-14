dict_carton = {"D001" : {"Brand" : "Duplex", "Category" : "Carton", "Mass" : "Gram", "Thickness" : 350},
                "P001" : {"Brand" : "Polyethilen", "Category" : "Plastic", "Mass" : "MicroMeter", "Thickness" : 5},
                "I001" : {"Brand" : "Ivory", "Category" : "Carton", "Mass" : "Gram", "Thickness" : 400},
                "K001" : {"Brand" : "ArtPaper", "Category" : "Carton", "Mass" : "Gram", "Thickness" : 190}}
carton_baru = {}

## Read Data
def read_data():
    if len(dict_carton) != 0:
        for m in dict_carton:
            print("Packaging Code : {}, Brand : {}, Category : {}, Mass : {}, Thickness : {}".format(m,dict_carton[m]["Brand"], dict_carton[m]["Category"], dict_carton[m]["Mass"], dict_carton[m]["Thickness"]))
        menu_read()
    else:
        print("Tidak Ada Data")
        menu_read()
def read_another_data():
    code = input("Masukan Kode Packaging: ").capitalize()
    if code in dict_carton.keys():
        print("Packaging Code : {}, Brand : {}, Category : {}, Mass : {}, Thickness : {}".format(code,dict_carton[code]["Brand"], dict_carton[code]["Category"], dict_carton[code]["Mass"], dict_carton[code]["Thickness"]))
        menu_read()
    else:
        print("-Tidak Ada Data Packaging-")
        menu_read()

# Menu Read Data
def menu_read():
    print("")
    print("*Packaging Data*")
    print("")
    print("1. Report Semua Data")
    print("2. Report Data Lainnya")
    print("3. Kembali ke Menu Utama")
    read_menu = input("Pilih Menu Read Data : ")
    if read_menu == "1":
        read_data()
    elif read_menu == "2":
        read_another_data()
    elif read_menu == "3":
        main_menu()
    else:
        menu_read()

# Create Data

# Menu Create
def menu_create():
    print("")
    print("**Menambah Data Packaging**")
    print("1. Tambah Data Packaging")
    print("2. Kembali ke Menu Utama")
    create_menu = input("Pilih Menu Create Data : ")
    if create_menu == "1":
        create_data()
    elif create_menu == "2":
        main_menu()
    else:
        menu_create()

# Create Data
def create_data():
    global new_code
    new_code = input("Masukan Code: ")
    if new_code in dict_carton.keys():
        print("Data Sudah Ada")
        menu_create()
    else:
        global a
        a = input("Masukan Brand: ")
        carton_baru["Brand"] = a
        global b
        b = input("Masukan Category: ")
        carton_baru["Category"] = b
        global c
        c = input("Masukan Mass: ")
        carton_baru["Mass"] = c
        global d
        d = int(input("Masukan Thickness: "))
        carton_baru["Thickness"] = d
        simpan_data()

# Simpan Data
def simpan_data():
    simpan_data_2 = input("Apakah Data Ingin Disimpan? (Yes/No): ").capitalize()
    global carton_baru
    global dict_carton
    if simpan_data_2 == 'Yes':
        print("Data Tersimpan")
        dict_carton[new_code] = carton_baru
        menu_create()
    if simpan_data_2 == 'No':
        print("Data Tidak Tersimpan")
        menu_create()
    else:
        simpan_data()

# Menu Update Data
def menu_update():
    print("")
    print("** Mengubah Data Packaging**")
    print("1. Ubah Data Packaging")
    print("2. Kembali Ke Menu Utama")
    update_menu = input("Pilih Menu Update Data: ")
    if update_menu == "1":
        check_data()
    elif update_menu == "2":
        main_menu()
    else:
        menu_update()

# Check Update Data
def check_data():
    global update_data
    update_data = input("Masukan Kode Packaging: ").capitalize()
    if update_data in dict_carton:
        print("Packaging Code : {}, Brand : {}, Category : {}, Mass : {}, Thickness : {}".format(update_data,dict_carton[update_data]["Brand"], dict_carton[update_data]["Category"], dict_carton[update_data]["Mass"], dict_carton[update_data]["Thickness"]))
        m = 1
        while m != 0:
            pilihan = input("Ketik Yes jika ingin Mengupdate Data atau No jika ingin cancel Update Data: ").capitalize()
            if pilihan == 'Yes':
                update_key = input("Masukkan Kolom atau Keterangan yang ingin di edit: ").capitalize()
                ubah_data = input("Masukkan {} Baru: ".format(update_key)).capitalize()
                m = 1
                while m != 0:
                    simpan_update = input("Apakah Data ingin di Update? (Yes/No): ").capitalize()
                    if simpan_update == 'Yes':
                        dict_carton[update_data][update_key] = ubah_data
                        print("Data Updated")
                        menu_update()
                        m = 0
                    elif simpan_update == 'No':
                        print("Data Tidak Terupdate")
                        menu_update()
                        m = 0
                    else:
                        m = 1
                menu_update()
            elif pilihan == "No":
                print("Data Tidak Terupdate")
                menu_update()
                m = 0
            else:
                m = 1
    else:
        print("Data Tidak Ditemukan")
        menu_update()            
    
def menu_delete():
    print("***Menghapus Data Packaging***")
    print("1. Hapus Data Packaging")
    print("2. Kembali Ke Menu Utama")
    delete_menu = input("Pilih Menu Delete Data: ")
    if delete_menu == "1":
        delete_data()
    elif delete_menu == "2":
        main_menu()
    else:
        menu_delete()

def delete_data():
    global delete_code
    delete_code = input("Masukkan Kode Karton: ").capitalize()
    if delete_code in dict_carton.keys():
        delete_data_notif()
    else:
        print("Data Tidak Ada")
        menu_delete()

def delete_data_notif():
    hapus_data = input("Apakah Data Ingin Dihapus? (Yes/No): ").capitalize()
    if hapus_data == "Yes":
        print("Data Terhapus")
        dict_carton.pop(delete_code)
        menu_delete()
    elif hapus_data == 'No':
        print("Data Tidak Terhapus")
        menu_delete()
    else:
        delete_data_notif()        

def main_menu():
    print("===== Stock Packaging ===== ")
    print(" ")
    print("1. Report Data")
    print("2. Menambah Data Packaging")
    print("3. Mengubah Data Packaging")
    print("4. Menghapus Data Packaging")
    print("5. Exit")
    main_menu_1 = input("Please Select Main Menu: ")
    if main_menu_1 == "1":
        menu_read()
    elif main_menu_1 == "2":
        menu_create()
    elif main_menu_1 == "3":
        menu_update()
    elif main_menu_1 == "4":
        menu_delete()
    elif main_menu_1 == "5":
        global exit
        exit = 0
        print("Thankyou for Order!")
        quit()
    else:
        print("***Pilihan yang anda masukkan salah***")
        main_menu()

main_menu()

    


            



