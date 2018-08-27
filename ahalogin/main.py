from test_case import play_ahain
from test_case import play_login
import sys
import csv
sys.path.append(sys.path[0])
filename = "C://Users/Administrator/Desktop/4.txt"
if __name__ == "__main__":
    # play_login.test_login("2823502386","960417?xc")

    # pwd = "88888888"
    # for i in range(1,16):
    #     name = "中移动广州"+str(i)+"号"
    #     play_ahain.test_ahain(name,pwd)

    # play_login.test_login()
    # with open(filename,'r') as fp:
    #     j=201
    #     for i in fp:
    #         play_ahain.test_ahain("Gz"+str(j),i)
    #         j+=1

    # for i in range(1,51):
    #     if i<10:
    #         play_ahain.test_ahain("aiqimo0"+str(i),"c++12345")
    #     else:
    #         play_ahain.test_ahain("aiqimo" + str(i), "c++12345")

    # with open(r'C:\Users\Administrator\Desktop\4.txt','r') as fp:
    #     j=1
    #     for i in fp:
    #         if j<10:
    #             play_ahain.test_ahain("Gz0"+str(j),i)
    #         else:
    #             play_ahain.test_ahain("Gz" + str(j), i)
    #         j+=1

    with open(r'C:\Users\Administrator\Desktop\7.txt','r') as fp:
        for i in fp:
            play_ahain.test_ahain("三阳路_"+i,"pythonlearning")



    # with open(r'C:\Users\Administrator\Desktop\7.txt','r') as fp:
    #     j=1
    #     for i in fp:
    #         if j<10:
    #             play_ahain.test_ahain("Gz0"+str(j),i)
    #         else:
    #             play_ahain.test_ahain("Gz" + str(j), i)
    #         j+=1
    #
