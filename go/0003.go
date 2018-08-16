package main

import (
  "fmt"
)


func main() {
  var a int
  var b int
  var c int
  var n int
  fmt.Scan(&n)
  for _, err := fmt.Scan(&a, &b, &c); err == nil; _, err = fmt.Scan(&a, &b, &c) {
    if a*a == b*b+c*c {
      fmt.Println("YES")
    } else if b*b == c*c+a*a {
      fmt.Println("YES")
    } else if c*c == a*a+b*b {
      fmt.Println("YES")
    } else {
      fmt.Println("NO")
    }
  }
}