import class_form as clf
import time as t

start_time_list = []
end_time_list = []
_classList = {}


def timeSplit(timeStr:str) -> tuple:
    _timeT = timeStr.split(":")
    return (int(_timeT[0]),int(_timeT[1]))

# 读取配置
def readInfo():
    try:
        with open("./class.csv",'r',encoding="utf-8") as f:
            # 读入配置文件，并将每行数据转为列表的一个元素
            rowData = f.readlines()
            # 第一行是星期
            firstRow = rowData[0]
            weekIndex = 0
            for week in firstRow[:-1].split(","):
                # 第一个数据固定为CLA
                if("CLA" not in week):
                    _classList[weekIndex] = "周" + week
                    weekIndex+= 1

            rowData.remove(firstRow)
            for element in rowData:
                # 去掉第一行后，每一行都是以时间段开头，后面接续每一个课程
                data = element[:-1].split(",")
                timeZone = data[0]
                # 处理时间，构建上课时间列表
                _timeZone = timeZone.split("~")
                start_time_list.append(timeSplit(_timeZone[0]))
                end_time_list.append(timeSplit(_timeZone[1]))
                data.remove(timeZone)
                dataIndex = 0
                # 构建课表字典
                for cla in data:
                    _classList[dataIndex] += cla
                    dataIndex += 1
            
            f.close()
    except FileNotFoundError:
        # 没有找到对应的文档，输出错误日志
        with open("./error_log_" + str(int(t.time())) + ".log" ,"w",encoding="utf-8") as f:
            f.write("[ERROR] 未找到课表文件，请在本程序目录下创建class.csv文件")

            f.close()




# 入口程序
if __name__ == '__main__':
    readInfo()
    clf.start_list = start_time_list
    clf.end_list = end_time_list
    clf.class_list = _classList
    clf.mainFunction()