# Design a function having no parameters but a return statement
w = 0


def water():
    global w
    w += 1
    return w


s = water()
print(w)
s = water()
print(s)
s = water()
print(s)
s = water()
print(s)
