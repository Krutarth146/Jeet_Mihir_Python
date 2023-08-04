# Functions are first class objects
# Function  can have inner Functions


def fun1():
    print("Inside fun1")

def fun2(f):
    print("Inside Fun2")
    f()

f = fun1
f()
print()

fun2(f)


# ---------------------
print("-----------------------")
def fun2():
    print("Inside fun2")

    def fun1():
        print("Inside fun1")

    fun1()

fun2()


# --------------------------------------------
print("-----------------")
def defun(f):
    def innerfun():
        print("Welcome")
        f()
    return innerfun

@defun
def fun():
    print("User")

# fun = defun(fun)
fun()