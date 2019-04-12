import csv
a = list(range(2550))
a.append('label')

css =  open('data.csv', 'a')
b=str(a).replace(']','').replace('[','').replace("'",'')
print(b)
css.write(b)
css.write('\n')
css.close()