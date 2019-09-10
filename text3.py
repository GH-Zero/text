
import xlrd
import os

path="text"

def readexcel():
    dable=xlrd.open_workbook('考生号码.xls')
    table=dable.sheets()[0]
    nrows=table.nrows
    for i in range(nrows):
        num=table.row_values(i)
        #print(num)
        filename=str(num[1])
        filename=os.path.join(path,filename)

        try:
            with open(filename,'w') as f:
                pass
                f.write(str(num))
        except Exception as e:
            print(e)

readexcel()
# def text_create(name, msg):
#     desktop_path = "E:/pycharm_pro/untitled1"
#     full_path = desktop_path +name + '.txt'
#     file = open(full_path,'w')
#     file.write(msg)
#     file.close()
#     print('Done')
# text_create('考生号码1', 'num')