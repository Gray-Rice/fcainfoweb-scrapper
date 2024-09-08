from datetime import date, timedelta

maxdate = date.today()-timedelta(days = 1)

def date_init(yr):
    global curdate, curyear, enddate
    curyear = yr
    curdate = date(yr,1,1)
    if(yr%4 == 0):
        enddate = curdate + timedelta(days = 366)
    elif(yr == 2024):
        enddate = maxdate
    else:
        enddate = curdate + timedelta(days=365)

def set_cus(date_in):
    global curdate
    curdate = date_in

def new_year():
    global curdate,curyear,enddate,maxdate
    curyear += 1
    curdate = date(curyear,1,1)
    if(curyear == 2024):
        enddate = maxdate
    elif(curyear %4 == 0):
        enddate = curdate + timedelta(days=366)
    else:
        enddate = curdate + timedelta(days=365)


def inc():
    global curdate,enddate
    if (curdate == maxdate):
        return None
    date_out =  curdate + timedelta(days = 1)
    if(date_out == enddate):
        new_year()
        return rdate()
    else:
        curdate = date_out
        return rdate()

def fdate(date_in):
    return date_in.strftime("%d/%m/%Y")

def rdate():
    global curdate
    return curdate
