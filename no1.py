import re
# list data
name = []
email = []
password = []
# regex
regex_email1 = r'@student[.]unhas[.]ac[.]id$'
regex_email2 = r'[A-Z]'
regex_email3 = r'[\s]'
regex_email4 = r'[!/,#$%^&*()_+=|{}[":;]'
regex_pw1 = r'[A-Z]'
regex_pw2 = r'[a-z]'
regex_pw3 = r'[\d]'
regex_file = r'Nama'
# function
def decoration(num):
    print('='*num)
def pw_lemah():
    print('Password yang Anda Masukkan Terlalu Lemah,')
    print('Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka')

while True:
    decoration(75)
    print('''Selamat Datang Silahkan Pilih Opsi Menu Anda
1. Detail Anda\n2. Ubah Nama\n3. Jumlah Data pada File
4. Save Data pada File\n5. Buat Data Baru\n6. Keluar''')
    opsi = input('Silahkan Pilih Opsi Anda : ')

    if opsi == '1':
        decoration(75)
        if name:
            print('Data anda adalah')
            for i in range(len(name)):
                print(f'Name : {name[i]}\nEmail : {email[i]}')
                print(f'Password : {password[i]}')
        else:
            print('Data Saat Ini Kosong')

    elif opsi == '2':
        decoration(75)
        if name:
            for i in range(len(name)):
                change = input(f'Silahkan Input Nama Baru Data ke-{i+1} : ')
                name[i] = change
        else:
            print('Data Saat Ini Kosong')
            
    elif opsi == '3':
        decoration(75)
        input_file = input('Silahkan Masukkan Nama File : ')
        try:
            with open(input_file + '.txt', 'r') as file:
                isi = file.read()
                total = isi.count(regex_file) # isi.count('Nama')
                print('Berhasil')
                print(f'Jumlah Data Pada File : {total} Data')
        except:
            print(f'Tidak Terdapat File Dengan Nama {input_file}.txt')
            print('Jumlah Data Pada File : 0 Data')
        
    elif opsi == '4':
        decoration(75)
        if name:
            input_file = input('Silahkan Masukkan Nama File: ')
            try:
                with open(input_file + '.txt', 'r') as file1:
                    file1.read()
            except:
                with open(input_file + '.txt', 'w') as file2:
                    file2.write('+'+'='*75)
                    file2.write('\n| Data yang Tersimpan')
                    file2.write('\n+'+'='*75)
                    
            with open(input_file + '.txt', 'a') as file3:
                for i in range(len(name)):
                    file3.write(f'\n| Nama           : {name[i]}')
                    file3.write(f'\n| Email          : {email[i]}')
                    file3.write(f'\n| Password       : {password[i]}')
                    file3.write('\n+' + '='*75)
            name.clear()
            email.clear()
            password.clear()
            print('Berhasil')
            
        else:        
            print('Data Saat Ini Kosong')
            
    elif opsi == '5':
        decoration(75)
        input_name = input('Silahkan Masukkan Nama Anda : ')
        name.append(input_name)
        
        while True:
            input_email = input('Silahkan Masukkan Email Anda : ')
            cek1 = re.search(regex_email1, input_email)
            if cek1:
                cek2 = re.findall(regex_email2, input_email)
                if cek2:
                    decoration(75)
                    print('Email yang Anda Masukkan Salah')
                    decoration(75)
                else:
                    cek3 = re.findall(regex_email3, input_email)
                    if cek3:
                        decoration(75)
                        print('Email yang Anda Masukkan Salah')
                        decoration(75)
                    else:
                        cek4 = re.findall(regex_email4, input_email)
                        if cek4:
                            decoration(75)
                            print('Email yang Anda Masukkan Salah')
                            decoration(75)
                        else:
                            email.append(input_email)
                            break
            else:
                decoration(75)
                print('Email yang Anda Masukkan Salah')
                decoration(75)
                
        while True:
            input_pw = input('Silahkan Masukkan Password Anda : ')
            if len(input_pw) >= 8 and len(input_pw) <= 20:
                cek1 = re.findall(regex_pw1, input_pw)
                if cek1:
                    cek2 = re.findall(regex_pw2, input_pw)
                    if cek2:
                        cek3 = re.findall(regex_pw3, input_pw)
                        if cek3:
                            password.append(input_pw)
                            break
                        else:
                            decoration(75)
                            pw_lemah()
                            decoration(75)
                    else:
                        decoration(75)
                        pw_lemah()
                        decoration(75)
                else:
                    decoration(75)
                    pw_lemah()
                    decoration(75)
            else:
                decoration(75)
                print('Password Harus Memiliki Panjang 8 - 20 karakter')
                decoration(75)
                
    elif opsi == '6':
        decoration(75)
        print('Sampai Jumpa Lagi')
        break
        
    else:
        decoration(75)
        print('Inputan Salah')
        print('Silahkan Masukkan Ulang Opsi')