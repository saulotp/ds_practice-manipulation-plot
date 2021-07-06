import pandas as pd


employee_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
client_df = pd.read_csv('CadastroClientes.csv', sep='\t',encoding='latin1')
services_df = pd.read_excel('BaseServiçosPrestados.xlsx')

#1. Total Payroll Value -> What was the total expenditure on employee salaries by the company?
payroll_df = employee_df['Salario Base'] + employee_df['Impostos'] + employee_df['Beneficios'] + employee_df['VT']+ employee_df['VR']
payroll_df = payroll_df.sum()
print(f'R$ {payroll_df:,.2f}')


#2. What was the company's revenue?
services_df = pd.merge(services_df, client_df)
services_df = services_df.drop(['Unnamed: 3'], axis=1)
display(services_df)
revenue_df = services_df['Tempo Total de Contrato (Meses)'] * services_df['Valor Contrato Mensal'] 
revenue_df = revenue_df.sum()
print(f'R$ {revenue_df:,.2f}')


#3. What is the % of employees who have already signed a contract?
employeecount_df = len(services_df['ID Funcionário'].unique())
employeetotalcount_df = len(employee_df['ID Funcionário'])
print(f'{employeecount_df*100/employeetotalcount_df:.2f}%')


#4. Calculate the total number of contracts that each area of the company has already signed.
area_df = pd.merge(services_df, employee_df)
print(area_df['Area'].value_counts())

import matplotlib.pyplot as plt
areaplot = area_df['Area'].value_counts()
areaplot.plot(kind='pie')


#5. Calculate total employees by area.
employeeplot_df = employee_df['Area'].value_counts()
employeeplot_df.plot(kind='pie')
print(employee_df['Area'].value_counts())


#6. What is the average monthly ticket (average monthly billing) of the contracts?
meanservice = services_df['Valor Contrato Mensal'].mean()
print(f'R$ {meanservice:,.2f}')
