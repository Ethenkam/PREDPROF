def readfile(namefile):
    '''

    :param namefile: csv file
    :return: max_comp list of company, maximum salary in this company and the vacancy in this company
    '''
    f=open(namefile, 'r', encoding='utf-8')
    vacancies=[]
    max_sal=0
    global max_comp
    max_comp=[]
    namecomp=[]
    for i in range(200):
        vacancies.append(f.readline().strip().split(';'))


    for i in range(200):
        if (vacancies[i][4] in namecomp)==False:
            namecomp.append(vacancies[i][4])
    for i in range(len(namecomp)):
        for j in range(1, 200):
            if namecomp[i]==vacancies[j][4]:
                if int(vacancies[j][2])>max_sal:
                    max_sal=max(int(vacancies[j][2]), max_sal)
                    max_comp.append([max_sal,namecomp[i],vacancies[j][3]])
    return(max_comp)
readfile('vacancy.csv')
max_comp.sort()
print(max_comp)
f=open('vacancy_new.csv', 'w')
f.write('company')
f.write(',')
f.write('role')
f.write(',')
f.write('Salary \n')
for i in range(3):
    f.write(str(max_comp[i][1]))
    f.write(',')
    f.write(str(max_comp[i][2]))
    f.write(',')
    f.write(str(max_comp[i][0]))
    f.write('\n')

