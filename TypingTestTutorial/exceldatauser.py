# Writing to an excel
# sheet using Python
from xlwt import Workbook
import xlrd
from xlutils.copy import copy

f1=open("rowcount.txt",'r')
var=f1.read()
count=int(var)

def myf(usernamefinal,correct,missing,mistakes,speed,resultf):
    global count
    count=count+1
    f1 = open("rowcount.txt", 'w')
    f1.write(str(count))
    print("data is saved")
    rb = xlrd.open_workbook("xlwt example.xls")
    wb = copy(rb)       #to copy xlrd.book object into an xlwt.workbook
    sheet1 = wb.get_sheet(0)
    v1=str(usernamefinal)

    v2=str(correct)
    v3=str(missing)
    v4=str(mistakes)
    v5=str(speed)
    v6=str(resultf)

# sheet1.write(row, column, 'CLOCK TOWER')
    print(count)
    sheet1.write(0, 0, 'user')
    sheet1.write(0, 1, 'correct')
    sheet1.write(0, 2, 'missing')
    sheet1.write(0, 3, 'mistakes')
    sheet1.write(0, 4, 'speed')
    sheet1.write(0, 5, 'result')
    sheet1.write(count, 0, v1)
    sheet1.write(count, 1, v2)
    sheet1.write(count, 2, v3)
    sheet1.write(count, 3, v4)
    sheet1.write(count, 4, v5)
    sheet1.write(count, 5, v6)




    wb.save('xlwt example.xls')
    return count
# myf(8,7,5,4,8)
# myf(9,9,9,9,9)
