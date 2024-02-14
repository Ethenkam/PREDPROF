def readfile(namefile):
    '''
    Чтение файла
    :param namefile: csv file
    :return: list with salary, company, vacancy and tye of job
    '''
    f=open(namefile, 'r', encoding='utf-8')
    global vacancies
    vacancies = []

    for i in range(200):
        vacancies.append(f.readline().strip().split(';'))
    return vacancies
readfile('vacancy.csv')
a=input()
c=0
while a!='None':
    for i in range(200):
        if vacancies[i][4]==a:
            print(f'В {vacancies[i][4]} найдена вакансия {vacancies[i][3]}. З/п составит {vacancies[i][2]}')
            c+=1
        if c==0 and i==199:
            print('К сожалению, ничего не удалось найти')
        if a=='None':
            break
    c=0
    a = input()
