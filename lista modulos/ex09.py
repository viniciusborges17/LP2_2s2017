def pego_correndo(speed, is_birthday):
    a=0
    if is_birthday:
        if (speed-5) <= 60:
            a = 0
        elif 60 < (speed-5) <= 80:
            a = 1
        else:
            a = 2
    else:
        if (speed) <= 60:
            a = 0
        elif 60 < (speed) <= 80:
            a = 1
        else:
            a = 2
    return a