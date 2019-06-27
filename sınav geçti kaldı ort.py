#mehmet şerif itak
#yazılı giriş alanı 3e bölünüp ortalama alınacak.

 
yazili1 = input('1. Yazılı Notu: ')
yazili2 = input('2. Yazılı Notu: ')
yazili3 = input('3. Yazılı Notu: ')
ortalama=(float(yazili1)+float(yazili2)+float(yazili3))/3
print("Ortalama :{0} ".format(ortalama))


#Çıkan ortalama sonucu öğrencinin geçti kaldı durumu öğrenilecek.
#50 altında kalırsa kalır üstü geçer.

if(int(ortalama)>=50):
      print("ÖĞRENCİ GEÇTİ")
else:
      print("ÖĞRENCİ KALDI")
