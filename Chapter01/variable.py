#变量用法
'''
name1 = "小明"
name1age=7
name1height=1.1
#print("你好，", name1)
#print('hello',name1)
name2='小张'
name2age=8
name2height=1.0
#print('nice to meet you',name,name2)
name3='teacher'
name3age=20
name3height=1.8
print(name1,':',name3,', nice to meet you ;')
print(name2,':',name3,', nice to meet you ;')
print(name3,': nice to meet you too ;')
print(name3,':',name1,'how old are you ?')
print(name1,':',name3,"I'm sever years old this year .")
print(name3,':',name2,'how tall are you ?')
print(name2,':',name3,"I'm one meter tall this year .")
'''

#数据类型 字符串、整数、浮点数
'''
print(type(name1))
print(type(name1age))
print(type(name1height))
#数据类型转换
a = 10
b = 3
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
'''
#input使用
'''
name4 = input("请输入名字 ： ")
print("输入的名字是： ",name4)
print(type(name4)) #str数据类型
#input是字符串类型，如需参与数字计算，比如强转为数字类型
name4_age = input('请输入年龄：')
print(type(name4_age)) #str格式
name4_age = int(name4_age)
print(type(name4_age)) #int整数类型
print("明年你的年龄：",name4_age + 1)
'''

# input综合练习

'''
print("==== 简单自我介绍 ====")
username = input("你的名字：")
user_age = int(input("你的年龄："))
user_height = float(input("你的身高(m)："))
print("==== 信息汇总 ====")
print("名字：", username)
print("年龄：", user_age)
print("10年后你的年龄：", user_age + 10)
print("身高类型：", type(user_height))
'''

#格式化输出
'''
#f-string用法，字符串前面加 `f`，大括号 `{}` 里面直接写变量名
name = "小张"
age = 12
height = 1.45345
# f-string
print(f"名字是：{name}，年龄是：{age}，五年后的年龄是：{age+5}，身高是{height:.3f}")
#.3f是指保留三位小数点
#格式化输出练习
# 格式化输出练习
username = input("请输入名字：")
user_age = int(input("请输入年龄："))
user_height = float(input("请输入身高："))
# f-string格式化输出
print(f"====个人信息====")
print(f"姓名：{username}")
print(f"年龄：{user_age} 岁")
print(f"身高：{user_height:.2f} m") #保留2位小数
'''

#if和else判断语句
'''
name5 = input('请输入名字：')
name5_age = int(input('请输入年龄：'))
if name5_age >= 18:
    print(f'恭喜{name5}, 您已经成年了！')
elif name5_age >= 12:
    print(f'{name5},你是青少年，你还有{18-name5_age}年就成年了！')
elif name5_age >= 6:
    print(f'{name5},你是儿童，你还有{12-name5_age}年就成为青少年了，还有{18-name5_age}年就成年了！')
else:
    print(f'{name5},你是幼儿，距离上小学还有{6-name5_age}年！')
'''

# and 并列判断语句
'''
name6 = input('请输入名字：')
name6_age = int(input('请输入年龄：'))
name6_hight = float(input('请输入身高：'))
if name6_age >= 12 and name6_hight >= 1.4:
    print(f'恭喜{name6}, 您可以去游乐园玩过山车了！')
else:
    print(f'{name6},你条件不符，不能玩！')
'''
# or 或者判断语句
'''
name7 = input('请输入名字：')
name7_age = int(input('请输入你的年龄：'))
name7_hight = float(input('请输入你的身高：'))
# 免票：6岁及以下 或 身高≤1.0 或 60岁及以上
if name7_age <= 6 or name7_hight <= 1.0 or name7_age >= 60 :
    print(f"{name7},你可以免票入内")
# 半票：6~12岁，并且身高≤1.2
elif (name7_age > 6 and name7_age <= 12) and name7_hight <= 1.2 :
    print(f"{name7},你可以半票")
else:
    print(f"{name7},你需要购买全票")
'''
#not 语句 not True 为 False ，not False 为 True
'''
# not 练习
is_holiday = input("今天是节假日吗？yes/no：")
# 不是节假日，才执行优惠
if not (is_holiday == "no"):
    print("节假日，可以享受折扣！")
else:
    print("非节假日，无折扣")
'''
#综合练习
# 1. 免票：**年龄≤6 岁 或者 年龄≥60 岁 或者 身高≤1.0m**
# 2. 半票：**6＜年龄≤12 并且 身高≤1.2m**，**并且不是节假日**
# 3. 其余情况：全票；
# 额外规则：节假日的时候，**取消半票优惠**（这里用 `not` 实现）
name8 = input("游客姓名：")
name8_age = int(input("游客年龄："))
name8_hight = float(input("游客身高："))
name8_holiday = input("今天是节假日嘛？ 请输入：y/n？")
if name8_age <= 6 or name8_age >= 60 or name8_hight <= 1.0 :
    print(f"{name8},你可以免票")
elif (name8_age > 6 and name8_age <= 12 ) and name8_hight <= 1.2 and not (name8_holiday == "y") :
    print(f"{name8},你可以半票")
else :
    print(f"{name8},你全票")
    
