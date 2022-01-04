// Successive approximations with Newton Method

def sqrtIter(guess: Double, x: Double): Double =
    if (isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)

def isGoodEnough(guess:Double, x:Double): Boolean =
    if (guess - x < 0.01) true else false

/** returns new guess*/
def improve(guess: Double, x: Double): Double =
    ((x/guess)+guess)/2
