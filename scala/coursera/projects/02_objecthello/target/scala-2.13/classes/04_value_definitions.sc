// call by name
def squareCBN(x:Double) = x*x

squareCBN(9)

//
def loop: Boolean = loop

// call by name the loop
// calls without evaluate and reduce interior
// value, so it finishes, it is ok
// to call loop like this
def x = loop

// call by value does not terminate,
// because it tries to reduce looop
// evaluates and evaluates loop until termination
// but it never terminates
//val x = loop
//
//x
//
//val j = 5