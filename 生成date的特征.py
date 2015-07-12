holiday = {}
holiday['20140101'] = 1
holiday['20140131'] = 1
holiday['20140201'] = 1
holiday['20140202'] = 1
holiday['20140203'] = 1
holiday['20140204'] = 1
holiday['20140205'] = 1
holiday['20140206'] = 1

holiday['20140405'] = 1
holiday['20140406'] = 1
holiday['20140407'] = 1


holiday['20140501'] = 1
holiday['20140502'] = 1
holiday['20140503'] = 1

holiday['20140602'] = 1
holiday['20140603'] = 1
holiday['20140604'] = 1

holiday['20140908'] = 1
holiday['20140909'] = 1
holiday['20140910'] = 1

holiday['20141001'] = 1
holiday['20141002'] = 1
holiday['20141003'] = 1
holiday['20141004'] = 1
holiday['20141005'] = 1
holiday['20141006'] = 1
holiday['20141007'] = 1

holiday['20130919'] = 1
holiday['20130920'] = 1
holiday['20130921'] = 1

holiday['20131001'] = 1
holiday['20131002'] = 1
holiday['20131003'] = 1
holiday['20131004'] = 1
holiday['20131005'] = 1
holiday['20131006'] = 1
holiday['20131007'] = 1

from datetime import timedelta, date
def give_date_feature(yyyymmdd):
    import datetime
    yyyy = int(yyyymmdd[0:4])
    mm = int(yyyymmdd[4:6])
    dd = int(yyyymmdd[6:])
    weekday = date(yyyy, mm, dd).weekday()

    isHoliday = [0]
    weekdayIndex = [0] * 7
    monthdayIndex = [0] * 31

    isHoliday[0] = holiday.get(yyyymmdd, 0)
    weekdayIndex[weekday] = 1
    monthdayIndex[dd-1] = 1

    feature = []
    feature.extend(isHoliday)
    feature.extend(weekdayIndex)
    feature.extend(monthdayIndex)
    return feature

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield (start_date + timedelta(n)).strftime("%Y%m%d")

features = {}
start = date(2013, 7, 1)
end = date(2014, 9, 1)
for yyyymmdd in daterange(start, end):
    features[yyyymmdd] = map(str, give_date_feature(yyyymmdd))

output = []
for key in sorted(features.keys()):
    output.append('%s, %s' % (key, ','.join(features[key])))
print 'output = c(\n%s)' % ',\n'.join(output)

