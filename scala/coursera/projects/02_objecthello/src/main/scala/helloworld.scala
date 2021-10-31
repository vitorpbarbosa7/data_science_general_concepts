
object HelloWorld extends App {
  def greet(name: String): Unit = {
    println(s"Hello, $name")
  }
  println("Hello World")
  greet(name = "AnnSa")
}