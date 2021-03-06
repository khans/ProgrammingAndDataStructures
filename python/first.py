import datetime
s = {
    "partners": [
        {
            "firstName": "Darin",
            "lastName": "Daignault",
            "email": "ddaignault@hubspotpartners.com",
            "country": "United States",
            "availableDates": [
                "2017-05-03",
                "2017-05-06"
            ]
        },
        {
            "firstName": "Crystal",
            "lastName": "Brenna",
            "email": "cbrenna@hubspotpartners.com",
            "country": "Ireland",
            "availableDates": [
                "2017-04-27",
                "2017-04-29",
                "2017-04-30"
            ]
        },
        {
            "firstName": "Janyce",
            "lastName": "Gustison",
            "email": "jgustison@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-29",
                "2017-04-30",
                "2017-05-01"
            ]
        },
        {
            "firstName": "Tifany",
            "lastName": "Mozie",
            "email": "tmozie@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-28",
                "2017-04-29",
                "2017-05-01",
                "2017-05-04"
            ]
        },
        {
            "firstName": "Temple",
            "lastName": "Affelt",
            "email": "taffelt@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-28",
                "2017-04-29",
                "2017-05-02",
                "2017-05-04"
            ]
        },
        {
            "firstName": "Robyn",
            "lastName": "Yarwood",
            "email": "ryarwood@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-29",
                "2017-04-30",
                "2017-05-02",
                "2017-05-03"
            ]
        },
        {
            "firstName": "Shirlene",
            "lastName": "Filipponi",
            "email": "sfilipponi@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-30",
                "2017-05-01"
            ]
        },
        {
            "firstName": "Oliver",
            "lastName": "Majica",
            "email": "omajica@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-28",
                "2017-04-29",
                "2017-05-01",
                "2017-05-03"
            ]
        },
        {
            "firstName": "Wilber",
            "lastName": "Zartman",
            "email": "wzartman@hubspotpartners.com",
            "country": "Spain",
            "availableDates": [
                "2017-04-29",
                "2017-04-30",
                "2017-05-02",
                "2017-05-03"
            ]
        },
        {
            "firstName": "Eugena",
            "lastName": "Auther",
            "email": "eauther@hubspotpartners.com",
            "country": "United States",
            "availableDates": [
                "2017-05-04",
                "2017-05-09"
            ]
        }
    ]
};

contents = s['partners'];
num = len(contents);

test = {}
countries = []
for each in contents:
    if each['country'] not in countries:
        countries.append(each['country'])
        test[each['country']] = [ [each['availableDates'],each['email']] ]
    else:
        test[each['country']].append([each['availableDates'],each['email']]);

#print (test['United States']);
newDict = {}
iDates = {}
dates = []


#print(dates)
'''for each in test['Spain']:
    if each[0]:
        for date in each[0]:
            if date not in dates:
                dates.append(date)
                iDates[date] = [1,[each[1]]]
            else:
                iDates[date][0] += 1
                iDates[date][1].append(each[1])
'''    


for key in test:
    for values in test[key]:
        if values[0]:                   #not an empty list of availableDates
            for date in values[0]:
                if date not in dates:
                    dates.append(date)
                    iDates[date] = [1,[values[1]]]
                else:
                    iDates[date][0] += 1
                    iDates[date][1].append(values[1])
    newDict[key] = iDates
    iDates = {}
    dates = []    


test = {}
print (newDict['Spain'])
print ('BREAK');
print (newDict['United States'])
print ('BREAK');
print (newDict['Ireland'])
results = []
tempD = {}    # will go in results



