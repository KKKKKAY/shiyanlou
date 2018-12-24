#!/usr.bin/env python3


import sys
import csv

class Args(object):
    
    def __init__(self,argv):
        self.argv=argv

    def checkArgv(self):
        args=self.argv[1:]
        path_dir={}
        if(len(args)==6):
            con_index=args.index("-c")
            con_path=args[con_index+1]
            path_dir["config"]=con_path
            
            user_index=args.index("-d")
            user_path=args[user_index+1]
            path_dir["user"]=user_path
            
            gz_index=args.index("-o")
            gz_path=args[gz_index+1]
            path_dir["gongzi"]=gz_path

        else:
            print("Parameter Error")
            
        return path_dir


class Config(object):
    
    def __init__(self,configPath):
        self.config=self._getConfigData(configPath)

    def _getConfigData(self,path):
        config={}
        filename=path
        
        with open(filename) as file:
            for x in file:
                config_data=x.split("=")
                config[config_data[0].strip()]=float(config_data[1].strip())

        return config
 

class UserData(object):

    def __init__(self,userPath):
        self.userdata=self._getUserData(userPath)

    def _getUserData(self,path):
        userdata={}
        filename=path
        
        with open(filename) as file:
            for x in file:
                if(x.count(",")==1):
                    user_data=x.split(",")
                    userdata[user_data[0].strip()]=float(user_data[1].strip())
                else:
                    print("USERDATA ERROR")
                    return None

        
        return userdata

class Calculator(object):
    
    def __init__(self,config,userdata):
        self.config=config
        self.userdata=userdata





if __name__=='__main__':
    
    args=Args(sys.argv)
    path=args.checkArgv()
    
    con=Config(path.get("config"))
    user=UserData(path.get("user"))
    
    
    if(con.config is not None and user.userdata is not None):
        print(user)
        print(type(user.userdata))





    
    


   

"""
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
"""
"""
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

"""



