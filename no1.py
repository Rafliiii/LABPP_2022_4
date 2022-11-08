class Orang:
    def __init__(self, nama, umur, gender,game):
        self.nama = nama
        self.umur = umur
        self.gender = gender
        self.game = game
    def getAge(self,umur):
        print(umur)
    def getName(self,nama):
        print(nama)
    def getGender(self,gender):
        if gender == True:
            gender = 'Male'
        else:
            gender = 'Female'
        print(gender)
    def bermain(self, game):
        print(f'{nama} sedang bermain game {game}')
nama = input('Masukkan nama: ').lower()
umur = int(input('Masukkan umur: '))
gender = input('you male? True or False: ').lower()
if gender == 'true':
    gender = bool(True)
else:
    gender = bool(False)
game = input('Masukkan game: ')
data_diri = Orang(nama, umur, gender, game)
data_diri.getName(nama)
data_diri.getAge(umur)
data_diri.getGender(gender)
data_diri.bermain(game)