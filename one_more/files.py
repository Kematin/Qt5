#Режимы чтения файла. 
#Основные: 
#r - чтение файлы, 
#w - перезапись файла, 
#a - добавление в файл. 
#Дополнительный: b - Binary mode



#Мини программа 
namefile = input("Введите название файла: ")

file2 = open(namefile, "r")

print("В файле " + namefile + " " + str(len(file2.read())) + " символов") #лен нужна для считывания кол-во символов

file2.close()


namefile = input("Введите желаемое имя файла(не забудьте добавить в конце расширение, например: .txt): ")
file = open(namefile, "w")
#Если файла нету он создаётся, если же он есть, то перезаписывается(т.е. удаляются все символы)


perez = input("Перезапиши файл: ")
file.write(perez) 
file.close()


file2 = open(namefile, "r")
print("В файле " + namefile + " " + str(len(file2.read())) + " cимволов")
file.close()


#Print(file.read(41))  В аргументе будет указано сколько байтов посчитает функция 

fl = open("newfile.txt", "w")
fl.write("Шалом папалом")
fl.close()



fl2 = open("newfile.txt", "r")
print(fl2.read(6))
print(fl2.read(7)) 
'''Полезно при ограничение памяти оперативки'''  
#Файл будет читатся с момента прошлого чтения, то-есть с 6 символа        
fl.close()




fil = open("test.txt", "w")
fil.close()

fil2 = open("test.txt", "a")
fil2.write("как дела?") 
'''Уже не перезапись а добавление, a = added'''


#Как читать файл по строкам?
fel = open("for_test.txt", "w")

fel.write("1 строка" + "\n")
fel.write("2 строка" + "\n")
fel.write("3 строка" + "\n")
fel.write("4 строка" + "\n")
fel.write("5 строка" + "\n")

fel.close()



fel2 = open("for_test.txt", "r")

string = fel2.readlines() #По сути создаётся список со всеми линяями


for stringrs in string:
	print(stringrs)

fel2.close()

#С помощью, with
for_test = open("for_test.txt", "w")
for_test.write("Привет, как дела?")
for_test.close()
with open("for_test.txt", "r") as f:
	print(f.read()) #С помощью временной переменой f мы прочитали файл
#После данных действий из-за with файл сразу закроется






