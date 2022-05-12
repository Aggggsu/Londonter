import random as rann
#Это бета версия* Если вы нашли ошибку: мой телеграм "@i2pd_anon_onionssss"
print("  v1.0, beta  ")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("")
print(" LONDON 2003 ")
print("")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
nameplay = input("Имя вашего персонажа:")
anooo = input("Лет вашему персонажу(а):")
print("Играть(start)")
what1 = input("/")
ogg = 1
warsss = (float(0))
Dollar = (float (1)) 
ban = (float (3)) 
press = (float (1)) 
ripp = (float (0))
norm = (float(0))
levelss =(float(1))
um = 2
umm = 30
ummm = 3
Police =(float(0))
Hotas = ("Пусто")
while what1 == "start":
  print("||||||||||||||||||||||||||||||||")
  print( str(nameplay) + ",Добро пожаловать в Лондон 2003 год.")
  print("Преступления:" + str(press))
  print("Блокнот:" + str(Hotas))
  print("Денег:" + str(Dollar))
  print("Убитых:" + str(ripp))
  print("Оружие:" + str(warsss))
  print("Банды:" + str(ban))
  print("Настроения, дела:" + str(norm))
  print ("Уровень:" + str(levelss))
  print("Уровень розыска:" + str(Police))
  print("|||||||||||||||||||||||||||||||")
  print("Что будешь делать? А:Заработать деньги, б:Что-то ограбить, д: создать банду, м:развлечения, магаз-магаз")
  what2 = input("/")
  if what2 == "а":
    print("**********************")
    print("Куда пойти работать?")
    print("А: кухня, б: магазин, в: мусоровоз :) ")
    print("**********************")
    what3 = input("/")
    if what3 == "а":
      if Police == 9:
        print("ffffffffffffffffffff")
        print("У вас:" + str(Police) +"! И вас поймали!")
        exit()
      else:
        print("Вам повезло с полицией! ")
      if Dollar == Dollar > 51:
        print("Вас приняли на работу!") 
        Dollar = Dollar - Dollar
        levelss = levelss + um
        norm = norm + ummm
      else:
        print("У вас недостаточно денег :) Нужно 51$")
    elif what3 == "б":
      if Police == 9:
        print("У вас:" + str(Police) +"! И вас поймали!")
        exit()
      else:
        print("Вам повезло с полицией! ")
      print("Вы вас есть документ о среднем образование?")
      print("**Автор: тсс, ты можешь соврать!**")
      whatshop1 = input("/")
      if whatshop1 == "да":
        print("Вас приняли!")
        levelss = levelss + um
        norm = norm + ummm
      else:
        print("Извините, уважаемый, нам вы не нужны!")
    elif what3 == "в":
      print("Вас без проблем преняли! ")
      Dollar = Dollar + um
      levelss = levelss + um
      norm = norm + ummm 
    else:
      print("Errrrrr :D")
  elif what2 == "б":
    Dollar = Dollar + umm
    Police = Police + ummm
    norm = norm - um
    if Police == 6:
      print("У вас:" + str(Police) +"! И вас поймали!")
      exit()
    else:
      print("Вам повезло с полицией! ")
    print("Поздравляю! У вас:" + str(Dollar))
    print("Но вас, возможно, отправлять в тюрьмы :( ...Ваш уровень розыска:" + str(Police))
  elif what2 == "д":
    print ("...........................")
    banname = input ("Название банды:")
    banpeople = input("Сколько людей 10/10:")
    print("Что будет делать ваша банда? Грабить(а), работать на полицейских(б)...")
    banwhat1 = input("/")
    if banwhat1 == "а":
      Dollar = Dollar + ummm
      Police = Police + um
      norm = norm + ummm
      ripp = ripp + umm
      press = press + um 
      print("Результат:")
      print("Банды:" + str(ban))
      print("Ваша банда:" + str(banname))
      print("Денег:" + str(Dollar))
      print("Убитых:" + str(ripp))
    elif banwhat1 == "б":
      print("Теперь вы не вор!")
      Police = Police - umm
      press = press - ummm
      levelss = levelss + ummm
      norm = norm + ummm 
      Dollar = Dollar + umm
    else:
      print("Errrrrr")
  elif what2 == "м":
    print("а - казино, б - шмотки, д - спорт,качалка, с - напечатать смс пацанам, т - телефон")
    whatm = input("/")
    if whatm == "а":
      print("Добро пожаловать в казино 777")
      print("начать (казино) ")
      cazwhat = input ("/")
      if cazwhat == "казино":
        print("крутится, крутится... ")
        cazz = rann.randint(10,15)
        if cazz == 8:
          print("Вы выиграли!")
          Dollar = Dollar + ummm
          norm = norm + ummm 
        else:
          print("Вы проиграли! Ваш результат" + str(cazz))
      else:
        print ("Errrrrr")
    elif whatm == "б":
      print("Вы точно хотите потратить деньги на какие-то шмотки? да/нет")
      smowhat = input("/")
      if smowhat == "да":
        print("Какие возьмёте: обычные, недорогие (а), дорогие, брендовые(б)")
        smowhat1 = input("/")
        if smowhat1 == "а":
          print("Поздравляю с покупкой!")
          Dollar = Dollar - um
          norm = norm + ummm
        elif smowhat1 == "б":
          print("Поздравляю с покупкой, петушок :)")
          Dollar = Dollar - ummm
          norm = norm + ummm 
        else:
          print("Errrrrr ")
      else:
        print("Согласен, тратить деньги на тряпки, такое себе...")
    elif whatm == "д":
      print("Добро пожаловать в спортзал!(начать)")
      whatsports = input("/")
      if whatsports == "начать":
        sporttplay = rann.randint(10,44)
        print("У вас закончилась тренировка...Результат:" + str(sporttplay))
        norm = norm + umm
      else:
        print("Errrrrr")
    elif whatm == "с":
      print("Список контактов:")
      print("--------------------")
      print("Братуха")
      print("Глава Банды")
      print("Старый дед")
      print("--------------------")
      SMS = input("Кому написать:")
      textsms = input("Текст:")
      smsrann1 = ["Привет, я занят.","Сколько можно повторять? Я - занят!","Да, ты уже надоел! ","Тебе делать ничего?"]
      smsrann2 = rann.choice(smsrann1 )
      if textsms == "Привет":
        print("Ответ от:" + str(SMS) + " Привет, у меня всё хорошо.")
      else:
        print("Сообщение:" + str(smsrann2))
    elif whatm == "т":
      print("--------------------")
      print("Меню телефона:")
      print("Нотатки,блокнот(а)")
      print("радио(б)")
      print("Часы(д)")
      print("--------------------")
      phone = input("/")
      if phone == "а":
        Hotas = input("Текст:")
        print("Текст сохранён")
      elif phone == "б":
        rannslo = ["London-radio","radioLS","RadioNY","Germany-mix-radio", 
        "France-vai-radio", "Bristol-radio","Epsom-radio"]
        radioo = rann.choice(rannslo)
        print("Сейчас играет:" + str(radioo))
      elif phone == "д":
        timephone = rann.randint(10, 23)
        print("Сейчас:" + str(timephone) + ":00")
      else:
        print("Errrrrr")
    else:
      print("Errrrrr :D")
  elif what2 =="магаз":
    print("Классические оружия(100$)")
    print ("Военные оружия(300$)")
    shoppingwar = input("1,2:")
    if shoppingwar == "1":
      if Dollar > 99:
        print("Поздравляю с покупкой! ")
        warsss = warsss + ogg
      else:
        print("У вас недостаточно денег!")
    elif shoppingwar == "2":
      if Dollar > 299:
        print("Поздравляю с покупкой! ")
        warsss = warsss + ogg
      else:
        print("У вас недостаточно денег!")
    else:
      print("Errrrrr")
  else:
    print("Errrrrr :D")
else:
  print("Errrrrr :D")
input()