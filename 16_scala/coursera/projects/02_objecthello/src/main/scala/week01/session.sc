// Successive approximations with Newton Method
object session {
  def sqrtIter(guess: Double, x: Double): Double =
    if (isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)

  def isGoodEnough(guess: Double, x: Double)=
    abs(guess * guess - x) < 0.001

  /** returns new guess */
  def improve(guess: Double, x: Double): Double =
    ((x / guess) + guess) / 2

  def abs(x: Double) = if (x<0) -x else x

  def sqrt(x:Double) = sqrtIter(1.0,x)
}

session.sqrt(2)
session.sqrt(4)
session.sqrt(9)