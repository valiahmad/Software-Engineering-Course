from jdatetime import datetime



def Time(year=0, month=0):

    year = datetime.today().year + year
    month = datetime.today().month + month
    day = datetime.today().day

    return str(year) + '/' + str(month) + '/' + str(day)
