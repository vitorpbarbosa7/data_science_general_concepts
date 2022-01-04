
object HelloWorld extends App {
  def greet(name: String): Unit = {
    println(s"Hello, $name")
  }
  println("Hello World")
  greet(name = "AnnSa")

  // and(x,y) == x && y
  def and(x: Boolean, y: Boolean):Boolean =
    if (x) y else false

  println("Correspondências")
  true && true
  and(true, true)
  print("--")
  false && true
  and(false, false)
  print("--")
  true && false
  and(true, false)
  print("--")
  false && false
  and(false, false)

  def or(x: Boolean, y: Boolean): Boolean = if (x) x else y

  println("Correspondências")
  true || true
  or(true,true)
  print("--")
  false || true
  or(false,true)
  print("--")
  false || true
  or(false,true)
  print("--")
  false || false
  or(false, false)
}

// and(x,y) == x && y
// def and(x: Boolean, y: Boolean):Boolean = {if (x) y else false}