import euler

term = 1
for x in euler.generate_fibbonaci():
    term += 1
    if len(str(x)) >= 1000:
        print term
        break
