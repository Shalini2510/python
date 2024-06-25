#CSV-- Comma seperated Values,  It is built in module

import csv
#csv.reader - file object as an argument and returns a list of list 

'''def csv_reader(fileobject):
    records =csv.reader(fileobject)
    for record in records:
        print(''.join(record))'''

#######   OR #######

def csv_dict_reader(fileobject):
    records= csv.DictReader(fileobject)
    for record in records:
        print(record['first_name'], record['last_name'])

if __name__ =="__main__":
    with(open("CSV/uk-500.csv","r")) as fh:
        #csv_reader(fh)
        csv_dict_reader(fh)




