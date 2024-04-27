
#This program calculates an employe's pay slip for a two week period


print('Name: ', end = '') #print comes first so it shows up first
name = input() #first name variable is declared
print('Total hours worked?: ', end ='') #print line comes up for the user to input total hours
num_hours = float(input()) #float is declared since decimal numbers are declared
print("Employee's hourly salary?: ", end='') #print line comes up for user to input the employee's hourly rate
standard_hour_rate = float(input()) #hourly wage is declared 

hours_pp = 80 # number of hours worked in a regular pay period





salary = num_hours*standard_hour_rate #how a regular salary is calculated before taxes are taken out

##calculate overtime
def overtimeCalculation(salary): 
    if num_hours > hours_pp:
        overtime_hours = num_hours - hours_pp
        overtime_pay = standard_hour_rate * 1.5 #in PA, OT rate is 1.5x
        overtime_salary = overtime_hours * overtime_pay
        return salary + overtime_salary #returns the salary + overtime paid hours for salary
    else:
        return salary #if hours worked is not greater than 80, it returns the salary


taxes = salary * 0.20 #tax rate is 20%
grossPay = salary - taxes #gross pay that employee takes home


##payslip

print(f'{"Employee Payslip":24}') #header
print(f'{"Name":^24}{"Hours Worked":^16}{"Gross Pay":^8}{"Taxes":^8}') #formats the headers of the payslip

print('-' * 72) #divides the header and actual payslip information

print(f'{name:<24}{num_hours:^16.2f}{grossPay:^8.2f}{taxes:^8.2f}') #formats the pay slip

