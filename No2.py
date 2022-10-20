print('Selamat datang untuk memulai silahkan input data anda')
nama = input('Input nama: ')
umur = int(input('Input umur: '))
alamat = input('Input alamat: ')
while True:
    print('==========================================================')
    print(f'Selamat datang {nama} silahkan pilih opsi')
    print('==========================================================')
    print('1. Detail anda')
    print('2. Ubah Nama')
    print('3. Ubah Umur')
    print('4. Ubah Alamat')
    print('5. Keluar')
    print('==========================================================')
    opsi = int(input('Input opsi: '))
    print('==========================================================')
    print('Data anda adalah')
    if opsi == 1:
        print(f'Nama: {nama}')
        print(f'Umur: {umur}')
        print(f'Alamat: {alamat}')
    elif opsi == 2:
        nama = input('Silahkan Input nama baru: ')
        print('Data anda sukses diperbarui')
    elif opsi == 3:
        umur = input('Silahkan Input umur baru: ')
        print('Data anda sukses diperbarui')
    elif opsi == 4:
        alamat = input('Silahkan Input alamat baru: ')
        print('Data anda sukses diperbarui')
    elif opsi == 5:
        print(f'selamat tinggal {nama} ')
        break
    else:
        print('Inputan salah')
