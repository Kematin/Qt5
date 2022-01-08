#Программа для копирования файлов

filename1 = input("Какой файл для создания точки сохранения?: ")
filename2 = "backup_" + filename1

file1 = open(filename1, "rb") #С помощью b можно копировать изображения, аудио и т.д.
file2 = open(filename2, "w")

file2.write(file1.read(1024 * 1000)) #Размер - 1 мб
file1.close()
file2.close()

print("Бэкап успешно завершён, нажмите Enter для выхода")
input()