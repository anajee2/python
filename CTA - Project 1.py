import pandas
import operator


# s = '/Users/abdullah/Desktop/School/MCS 275/Lecture Practice/CTA_-_Ridership_-__L__Station_Entries_-_Daily_Totals.csv'


class DataSet(object):
    def __init__(self, file_name):
        self.fn = file_name
        self.data = pandas.read_csv(self.fn, names=['station_id', 'name', 'date', 'daytype', 'rides'], skiprows=[0])
        self.dict = self.data.to_dict()

    def get_column(self, column_name):
        return self.data[column_name].tolist()


def getWeekday(year, month, day):
    """
    input: integers year, month, day
    output: name of the weekday on that date as a string
    """
    import datetime
    import calendar
    date = datetime.date(year, month, day)
    return calendar.day_name[date.weekday()]


def assignment2(data):
    dates = data.get_column('date')
    rides = data.get_column('rides')
    station = data.get_column('station_id')
    months = {'January': [], 'February': [], 'March': [], 'April': [], 'May': [], 'June': [], 'July': [], 'August': [],
              'September': [],
              'October': [], 'November': [], 'December': []}
    for i in range(len(dates)):
        if station[i] == 40350:
            d = dates[i].split("/")
            month = d[0]
            r = rides[i]
            if month == '1':
                months['January'].append(r)
            if month == '2':
                months['February'].append(r)
            if month == '3':
                months['March'].append(r)
            if month == '4':
                months['April'].append(r)
            if month == '5':
                months['May'].append(r)
            if month == '6':
                months['June'].append(r)
            if month == '7':
                months['July'].append(r)
            if month == '8':
                months['August'].append(r)
            if month == '9':
                months['September'].append(r)
            if month == '10':
                months['October'].append(r)
            if month == '11':
                months['November'].append(r)
            if month == '12':
                months['December'].append(r)

    for m in months:
        total = 0
        arr = months[m]
        for v in arr:
            total += int(v)
        avg = total / len(arr)
        print(m, ': ', float(avg))


def assignment3(data):
    dates = data.get_column('date')
    rides = data.get_column('rides')
    station = data.get_column('station_id')
    days = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
    for i in range(len(dates)):
        if station[i] == 40350:
            d = dates[i].split("/")
            month = int(d[0])
            day = int(d[1])
            year = int(d[2])
            r = rides[i]
            weekday = getWeekday(year, month, day)
            days[weekday].append(r)

    ridesinorder = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}

    for d in days:
        total = 0
        arr = days[d]
        for a in arr:
            total += int(a)
        ridesinorder[d] = total

    ridesinorder = sorted(ridesinorder.items(), key=operator.itemgetter(1))

    print(ridesinorder)

    print("Busiest Day: ", ridesinorder[-1])
    print("Least Busy Day: ", ridesinorder[0])
    print('Rides on wednesday', ridesinorder[-1])



'''
This main function holds assignment one
'''


def main():
    Data = DataSet('CTA_-_Ridership_-__L__Station_Entries_-_Daily_Totals.csv')
    print(Data.data)
    assignment2(Data)
    assignment3(Data)


main()