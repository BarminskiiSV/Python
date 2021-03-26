from csv import *
import sys

filename = str(sys.argv[1])
period1 = str(sys.argv[2])
period2 = str(sys.argv[3])

period1 = period1.replace('-', '')
period1 = period1.replace('Т', '')
period1 = int(period1.replace(':', ''))

period2 = period2.replace('-', '')
period2 = period2.replace('Т', '')
period2 = int(period2.replace(':', ''))

num = 0

totaltopuptries = 0
totalscooptries = 0
topupfails = 0
scoopfails = 0
topupvolume = 0
scoopvolume = 0
topupfailsvolume = 0
scoopfailsvolume = 0
topupvolume1 = 0
scoopvolume1 = 0
currentvolume = 0

log = open(filename, 'r')
for i in log.readlines():
    if num == 2:
        currentvolume = int(i[:i.find("(")])
    if num > 2:
        time = i.find(".")
        time = i[:time]
        time = time.replace('-', '')
        time = time.replace('Т', '')
        time = int(time.replace(':', ''))

        if time >= period1 and time <= period2:
            if i.find("top up") != -1:
                totaltopuptries = totaltopuptries + 1
                if i.find("успех") != -1:
                    ind = i.find("top up") + 7
                    litres = int(i[ind:i.find("l")])
                    topupvolume = topupvolume + litres
                elif i.find("фейл") != -1:
                    topupfails = topupfails + 1
                    ind = i.find("top up") + 7
                    litres = int(i[ind:i.find("l")])
                    topupfailsvolume = topupfailsvolume + litres
            elif i.find("scoop") != -1:
                totalscooptries = totalscooptries + 1
                if i.find("успех") != -1:
                    ind = i.find("scoop") + 6
                    litres = int(i[ind:i.find("l")])
                    scoopvolume = scoopvolume + litres
                elif i.find("фейл") != -1:
                    scoopfails = scoopfails + 1
                    ind = i.find("scoop") + 6
                    litres = int(i[ind:i.find("l")])
                    scoopfailsvolume = scoopfailsvolume + litres
        elif time > period2:
            if i.find("top up") != -1:
                if i.find("успех") != -1:
                    ind = i.find("top up") + 7
                    litres = int(i[ind:i.find("l")])
                    topupvolume1 = topupvolume1 + litres
            elif i.find("scoop") != -1:
                if i.find("успех") != -1:
                    ind = i.find("scoop") + 6
                    litres = int(i[ind:i.find("l")])
                    scoopvolume1 = scoopvolume1 + litres

    num = num + 1

topupfails = (100*topupfails)/totaltopuptries
scoopfails = (100*scoopfails)/totalscooptries
period2volume = currentvolume - topupvolume1 + scoopvolume1
period1volume = period2volume - topupvolume + scoopvolume
print(totaltopuptries, totalscooptries, topupfails, scoopfails, topupvolume, scoopvolume, topupfailsvolume, scoopfailsvolume, period1volume, period2volume)


print('====При налитии воды====')
print('Количество попыток налить воду за указанный период: ' + str(totaltopuptries))
print('Процент ошибок за указанный период: ' + str(topupfails))
print('Объем налитой воды в бочку за указанный период: ' + str(topupvolume))
print('Объем воды, который был не налит в бочку за указанный период: ' + str(topupfailsvolume) + '\n')

print('====При заборе воды====')
print('Количество попыток извлечь воду за указанный период: ' + str(totalscooptries))
print('Процент ошибок за указанный период: ' + str(scoopfails))
print('Объем извлеченной воды из бочки за указанный период: ' + str(scoopvolume))
print('Объем воды, который был не извлечен из бочки за указанный период: ' + str(scoopfailsvolume) + '\n')

print('Объем воды в начале указанного периода: ' + str(period1volume))
print('Объем воды в конце указанного периодаЖ ' + str(period2volume))

print("Нажмите Enter!")
input()