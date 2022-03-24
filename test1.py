"""
 * Project name(项目名称)：Python嵌套循环实现冒泡排序
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:57
 * Version(版本): 1.0
 * Description(描述)： 
 """
import random

if __name__ == '__main__':
    data = []
    i = 0
    while i < 40:
        r = random.randint(0, 500)
        data.append(r)
        i = i + 1
    print(data)
    # 实现冒泡排序
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print("排序后：", data)
