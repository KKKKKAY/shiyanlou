#!/usr.bin/env python3


import sys

def insured_count(salary):
    insured=""
    old=0.08
    hos=0.02
    job=0.005
    hurt=0
    born=0
    home=0.06
    insured=salary*(old+hos+job+hurt+born+home)
    
    return format(insured,'.2f')


def tax_count(salary,insured):
    
        tax=""
        baseSalary=3500
        
        gapSalary=salary-insured-baseSalary
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
        return format(tax,".2f")


if __name__=='__main__':
    if(len(sys.argv)>=2):
        output_item={}
        for input_item in sys.argv[1:]:
            item=input_item.split(':')
            name=item[0]
            try:
                salary=int(item[1])
            except ValueError:
                print("Parameter Error")
            
            insured_fee=float(insured_count(salary))       
            tax_fee=float(tax_count(salary,insured_fee))
            salary_after_tax=salary-insured_fee-tax_fee
            output_item[name]=format(salary_after_tax,'.2f')
        
        
        
        for key,value in output_item.items():
            print("{}:{}".format(key,value))
    else:
        print("Parameter Error")





