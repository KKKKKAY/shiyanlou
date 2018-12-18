#!/usr.bin/env python3

import sys

if(len(sys.argv)==2):
    salary=sys.argv[1]
    # print(salary)
    try:
        salaryInt=int(salary)
        tax=""
        baseSalary=3500
        gapSalary=salaryInt-baseSalary
        if(gapSalary>0 and gapSalary<=1500):
            tax=gapSalary*0.03
        elif(gapSalary>1500 and gapSalary<=4500):
            tax=gapSalary*0.1-105
        elif(gapSalary>4500 and gapSalary<=9000):
            tax=gapSalary*0.2-555
        elif(gapSalary>9000 and gapSalary<=35000):
            tax=gapSalary*0.25-1005
        elif(gapSalary>35000 and gapSalary<=55000):
            tax=gapSalary*0.3-2755
        elif(gapSalary>55000 and gapSalary<=80000):
            tax=gapSalary*0.35-5505
        elif(gapSalary>80000):
            tax=gapSalary*0.45-13505
        else:
            tax=0
        print(format(tax,".2f"))
    except ValueError:
        ("Parameter Error")
    
        
else:
    print("Parameter Error")
    
