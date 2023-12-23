import Algorithm
from colorama import Fore
print(Fore.GREEN+"Firstly we must make sorting , after we will do searching"+Fore.RESET)
ask=list(map(int,input("write your list of numbers: ").split()))
h=Algorithm.selection_sort(ask)
print(f"sorted list: {h}")
print(Fore.GREEN+"Now we will do searching"+Fore.RESET)
ask2=int(input("which number do u want to be found: "))
Algorithm.binary_search(h,ask2)
