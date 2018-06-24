import csv
class CsvFileManger2:
    @classmethod
    def read(self):
        path=r'C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv'
        file=open(path,'r')
        #通过CSV代码库读取打开的CSV文件，获取文件中所有数据
        data_table=csv.reader(file)
        #for循环  item是每一行  in 在数据集中  data_table表示数据集
        #data_table有几行数据，就会执行几次
        for item in data_table:
            print(item)

if __name__ == '__main__':
    #csvr=CsvFileManger2()
    #csvr.read()
#方法上面加上@classmethod ，表示这个方法可以直接用类调用.. 不需要先实例化对象后才能调用
    CsvFileManger2.read()