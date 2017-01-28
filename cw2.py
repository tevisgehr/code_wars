def calculate_years(pv, i, t, fv):
    years = 0
    while pv < fv:
        pv += (pv*i)-(pv*i*t)
        years +=1

    return years
