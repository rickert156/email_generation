import csv
import os

search_files = os.listdir()
list_dirs = []
for search_file in search_files:
    if '.csv' in search_file:list_dirs += [search_file]

num=0
for list_dir in list_dirs:
    num+=1
    print(f'[{num}] {list_dir}')

enter_list = int(input('Введите значение: '))
enter_list-=1
try:
    document = (list_dirs[enter_list])
    print(document)

    with open(document, 'r') as file_csv:
        for row in csv.DictReader(file_csv):
            row_name = row['name']
            row_domain = row['domain']
            row_company = row['company']
            if ' ' in row_name:
                first_name, last_name = row_name.split(' ')
                option_1 = f'{first_name.lower()}.{last_name.lower()}@{row_domain}'
                option_2 = f'{last_name.lower()}.{first_name.lower()}@{row_domain}'
                option_3 = f'{first_name.lower()}{last_name.lower()}@{row_domain}'
                option_4 = f'{last_name.lower()}{first_name.lower()}@{row_domain}'
                option_5 = f'{first_name.lower()}@{row_domain}'
                print(option_1, row_company)
                print(option_2, row_company)
                print(option_3, row_company)
                print(option_4, row_company)
                print(option_5, row_company)
                column = f'{row_name},{row_company}'
                with open('result.csv', 'a+') as result_file:
                    result_file.write(f'{column},{option_1}\n{column},{option_2}\n{column},{option_3}\n{column},{option_4}\n{column},{option_5}')
            else:
                result_email = f'{row_name.lower()}@{row_domain}'
                print(result_email, row_company)
                column = f'{row_name.lower()},{row_company}'
                with open('result.csv', 'a+') as result_file:
                    result_file.write(f'{column},{result_email}\n')

except:print('Некорректный выбор')       

