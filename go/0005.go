package main

import (
  "fmt"
)

func gcd(a, b int) int {
  if b == 0 {
      return a
  }
  return gcd(b, a%b)
}

func main() {
  var a,b,c int
  for _, err := fmt.Scan(&a, &b); err == nil; _, err = fmt.Scan(&a, &b) {
    c = gcd(a,b)
    fmt.Println(c, a*b/c)
  }
}