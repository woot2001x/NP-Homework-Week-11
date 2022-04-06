# Network Performance Homework Week 11 (Problem-6)
from math import e
def cs1():
    #มีโอกาสกี่ % ที่แต่ละ Client ต้องรอรับบริการนานกว่า 20 วินาที
    min_wait_time = 0
    max_wait_time = 30
    x = max_wait_time - 20
    ans = (x-min_wait_time)/(max_wait_time-min_wait_time)
    print(str("%.2f"%(ans*100)) + "%")
cs1()

def cs2():
    #เวลาเฉลี่ยที่แต่ละ Client ต้องรอรับบริการ
    min_wait_time = 0
    max_wait_time = 30
    ans = (min_wait_time+max_wait_time)/2
    print(str(ans) + " seconds")
cs2()

def cs3():
    #มีโอกาสกี่ % ที่แต่ละ Client ทำงานเสร็จภายใน 25 วินาที
    request_time_prob = 15/30
    l = 1/10
    service_time_prob = 1 - (e**(-l*10))
    ans = request_time_prob*service_time_prob
    print(str("%.2f"%(ans*100)) + "%")
cs3()

def cs4():
    #เวลาเฉลี่ยที่แต่ละ Client ทำงานจนเสร็จ
    avg_request_time = 15
    avg_service_time = 10
    ans = avg_request_time+avg_service_time
    print(str(ans) + " seconds")
cs4()