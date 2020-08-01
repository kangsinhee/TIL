import datetime

now = datetime.datetime.now()

nowDatetime = now.strftime('%Y.%m.%d %H:%M:%S')
nowDate = now.strftime('%Y.%m.%d')
nowtime = now.strftime('%H'+'시 '+'%M' + '분 ' + '%S' +'초')


timestr = '2020-07-29 23:32:09'
setDatetime = datetime.datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S')
setDate = setDatetime.strftime('%Y.%m.%d')
settime = setDatetime.strftime('%H'+'시 '+'%M' + '분 ' + '%S' +'초')

print('Now_time')

print(now)
print(nowDatetime)
print(nowDate)
print(nowtime)

print('-----------------')

print('Set_time')

print(setDatetime)
print(setDate)
print(settime)
