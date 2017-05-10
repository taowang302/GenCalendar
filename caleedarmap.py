#-*- coding: UTF-8 -*-
import datetime

def is_leap_year(year):  
    # 判断是否为闰年  
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  
        return True  
    else:  
        return False  
  
  
def get_num_of_days_in_month(year, month):  
    # 给定年月返回月份的天数  
    if month in (1, 3, 5, 7, 8, 10, 12):  
        return 31  
    elif month in (4, 6, 9, 11):  
        return 30  
    elif is_leap_year(year):  
        return 29  
    else:  
        return 28  
  
  
def get_total_num_of_day(year, month):  
    # 自1800年1月1日以来过了多少天  
    days = 0  
    for y in range(1800, year):  
        if is_leap_year(y):  
            days += 366  
        else:  
            days += 365  
  
    for m in range(1, month):  
        days += get_num_of_days_in_month(year, m)  
  
    return days  
  
  
def get_start_day(year, month):  
    # 返回当月1日是星期几，由1800.01.01是星期三推算  
    return 3 + get_total_num_of_day(year, month) % 7  

def get_input_day(day,_rest=2,_step=3):
    week_list = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
    now_date = datetime.datetime.now().strftime('%m-%d-%a-%Y').split('-')
    now_month = int(now_date[0])
    now_day = int(now_date[1])
    now_week = now_date[2]
    index_week = week_list.index(now_week)
    if now_day == day:
        input_week = now_week
        index_input_week = index_week
    elif now_day > day:
        index_input_week = abs((index_week - (now_day - day)%7)%7)
        input_week = week_list[index_input_week]
    else:
        index_input_week = abs((index_week + (day - now_day)%7)%7)
        input_week = week_list[index_input_week]

    #print input_week,index_input_week

    print_month_title(now_date[3],now_month)      
    print_month_body(now_date[3],now_month,day,index_input_week,set_work_list(_rest,_step))

  
  
# 月份与名称对应的字典  
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',  
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}  
  
  
def get_month_name(month):  
    # 返回当月的名称  
    return month_dict[month]  
  
  
def print_month_title(year, month):  
    # 打印日历的首部  
    print '         ', get_month_name(month), '   ', year, '          '  
    print '-------------------------------------'  
    print '  Sun   Mon  Tue   Wed   Thu   Fri   Sat  '  
  
def set_work_list(_rest,_step):
    work_list = ['夜']
    for i in range(_rest):
        work_list.append('休')
    for j in range(_step):
        if j == _step - 1:
            work_list.append('早')
        else:
            work_list.append('班')
    return work_list
  
def print_month_body(year,month,day,inx,work_list):  
    ''''' 
    打印日历正文 
    格式说明：空两个空格，每天的长度为5 
    需要注意的是print加逗号会多一个空格 
    '''
    month_list = ['一','二','三','四','五','六','七','八','九','十','十一','十二']  
    #work_list = [ '夜','休','班' ]
    w = 0
    l = len(work_list)
    if inx >0:  
        print '', # 打印行首的两个空格  
        #if day >=10:
            #print 
        for i in range(inx-1):
            print '     ',
        print'    ' ,  # 从星期几开始则空5*几个空格  
    for j in range(day, get_num_of_days_in_month(year, month)+1):  
        if j == 1:
            print '%4s/%s' %(month_list[int(month) - 1],'夜'),
        else:
            print '%2d/%s' %(j,work_list[w % l]), # 宽度控制，4+1=5  
        inx += 1
        w += 1  
        if inx % 7 == 0:  # i用于计数和换行  
            print ' '   # 每换行一次行首继续空格  
  
  
#   主函数部分  
#month = int(raw_input("Please input target month:"))  
week = int(raw_input("Please input target week:"))
get_input_day(int(week))