from configparser import ConfigParser
import random
class GuessGameBox():
    config_object = ConfigParser()
    config_object["DEFAULT"] = {
        "numbermax" : "6",
        "randommax" : "4"
    }
    config_object["EASY"] = {
        "numbermax" : "9",
        "randommax" : "4"
    }
    config_object["NORMAL"] = {
        "numbermax" : "50",
        "randommax" : "6"
    }
    config_object["HARD"] = {
        "numbermax" : "100",
        "randommax" : "10"
    }
    with open("config.ini", "w") as conf:
        config_object.write(conf)

    config_object.read("‪config.ini")
    level = config_object["EASY"]      # DEFAULT, EASY, NORMAL, HARD
    numbermax = int(level["numbermax"])
    randommax = int(level["randommax"])
    number = list(range(1, numbermax+1))
    # print(number)
    # print(numbermax)
    # print(randommax)
    lst = []
    lst_n = []
    def main(self):
        print("""
                GuessingGame!
                    Menu
                1.New Play
                2.Exit
        """)
        n = input("Choose 1-2: ")
        if n == "1":
            if start.lst == [] and start.lst_n == []:
                start.random_list()
                print(start.lst)      #แสดงผล random lst
                start.guess()
            elif start.lst != [] and start.lst_n !=[]:
                start.lst.clear()
                start.lst_n.clear()
                start.random_list()
                print(start.lst)
                start.guess()
        elif n == "2":
            exit
        else:
            print("Please Enter 1-2")
            return start.main()
    def random_list(self):
        rd = random.sample(start.number, start.randommax)
        start.lst = rd
    def guess(self):
        for i in range(start.randommax):
            n = int(input("Enter number 1-%d Rows %d:%d: " %(start.numbermax, i+1, start.randommax)))
            start.lst_n.append(n)
        print("My list", start.lst_n)
        for i in range(start.randommax):
            if start.lst_n[i] == start.lst[i]:
                print("□", end=" ")
            elif start.lst_n[i] != start.lst[i]:
                print("■", end=" ")
        print()
        start.check()
    def check(self):
        for i in range(start.randommax):
            if start.lst_n[i] == start.lst[i]:
                pass
            elif start.lst_n[i] != start.lst[i]:
                start.lst_n.clear()
                return start.guess()
        print("You Win")
        return start.main()


start = GuessGameBox()
start.main()
