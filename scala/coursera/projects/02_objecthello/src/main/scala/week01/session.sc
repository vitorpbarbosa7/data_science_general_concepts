// Successive approximations with Newton Method
object session {
  def sqrtIter(guess: Double, x: Double): Double =
    if (isGoodEnough(guess, x)) guess
    else sqrtIter(improve(guess, x), x)

  def isGoodEnough(guess: Double, x: Double): Boolean =
    if (abs(guess*guess - x) < 0.001)

  /** returns new guess */
  def improve(guess: Double, x: Double): Double =
    ((x / guess) + guess) / 2
}