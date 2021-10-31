val b = false

val _true = "true"
val _false = "false"

println("original expression")
if (b) true else false

println("rewrite rule")
true && b || false && b

println("professor:")