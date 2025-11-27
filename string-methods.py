upper()  # bütün karakterleri büyütür.
lower()  # bütün karakterleri küçültür.
title()  # bütün kelimelerin başharfi büyür.
capitalize() # stringin ilk harfini büyütür.
strip() # baş ve sondaki boşlukları siler.
split() # stringini boşluklardan yada belirttiğimiz ifadeden ayırarak kelime dizisine dönüştürür.
' '.join(message)  #split ile yada mevcul olan bir kelime arrayini birleştirmek için kullanırız. ' ' birleştirirken aralara ne konulacak söylediğimiz yer. message de array.
find('hakan')  # stringde aramak istediğimiz kelimeyi bulmak için kullanırız. buradan kelime varsa ilk harfin string içerisindeki index değeri döner.
replace('hakan','doruk')   # string içersinde değiştirmek istediğimiz karakter yada kelimeyi bu şekilde değiştiririz
center(100)   # 100 karakterlik bir alan oluşturur ve stringi ortasına yazar. 
