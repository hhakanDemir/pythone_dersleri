# STRING KONUSUNDA SORU COZUMLARI


website = "http://www.sadıkturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehperiniz (40 saat)"


#1 'course' karater dizisinde kaç karakter bulunmaktadır?

result = len(course)

#2 'website' içerisinden www karakterlerini alın.

result = website[7:10]

#3 'website' içerisinden com karakterlerini alın.

result = website[22:25]

length = len(website)
result = website[length-1 : length]

#4 'course' içerisiniden ilk 15 ve son 15 karakterini alın.

result = course[:15]   # : dan önce sayı yazmazsak random 0 dan başlar.
result = course[-15:]  # stringlerde sondan başlarsak -1 -2 ... diye sayarız. Bu örnekte : dan sonra -1 yazınca son karakteri almadı. O yüzden boş bıraktık.

#5 'course' ifadesindeki karakterleri tersten yazdırın.

result = course[::-1]

nama, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

#6 Yukarıdaki verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın. 
#  "Benim adım Bora Yılmaz, Yaşım 32 ve Mesleğim mühendis"

result = "Benim adım " + name + " " + surname + " Yaşım " + str(age) + " ve Mesleğim " + job
result = 'Benim adım {0} {1}, Yaşım {2} ve Mesleğim {3}'.format(name,surname,age,job)
result = f"Benim adım {name} {surname}, Yaşım {age} ve Mesleğim {job}"

#7 'Hello world' ifadesindeki w karfini W ile değiştirin.

s = 'Hello world'
result = s[0:6] + 'W' + s[-4:]

#8 'abc ifadesini yan yana 3 defa yazdırın'

result = 'abc' * 3















