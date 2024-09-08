import csv

def csv_init():
    f = open("header.txt","r")
    header = f.readline().strip().split(",")
    f.close()
    with open("data.csv","w") as f:
        cw = csv.writer(f)
        cw.writerow(header)
        f.close()
    return


def saverow(row):
    with open("data.csv","a") as f:
        cw = csv.writer(f)
        cw.writerow(row)
        f.close()
    return
