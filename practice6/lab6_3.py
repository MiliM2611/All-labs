# 6.3

def magicDate(date):
    if int(date[0:2]) * int(date[3:5]) == int(date[8:10]):
        return True
    else:
        return False

date = str(input())
print(magicDate(date))