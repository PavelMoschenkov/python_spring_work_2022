#  Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm
#
# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
# "EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#
# Каждое значение из списка должно находится на отдельной строке.


algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori",
            "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]

a = len(algoritm)

f = open("algoritm.csv", "w+")

for i in range(0, a):
    f.writelines("- id - № " + str(i+1) + " " + algoritm[i] + "\n")

f.close()
