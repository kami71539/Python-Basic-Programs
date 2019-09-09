# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:45:41 2019

@author: Kamran
"""

#employee_file=open("employees.txt","r")
#employee_file=open("employees.txt","a")
employee_file=open("employees.txt","w")
'''print(employee_file.readable())
#print(employee_file.read())
print(employee_file.readline())
print(employee_file.readlines()[1])
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
for employee in employee_file.readlines():
    print(employee)'''
#open("employees.txt",w)  
employee_file.write("Kelly - IT")
#open("employees.txt",r+)
employee_file.close
