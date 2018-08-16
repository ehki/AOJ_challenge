package main

import (
  "fmt"
)

func main() {
  var a int
  var b int
  b = 100000
  fmt.Scan(&a)
  for i:= 0; i<a; i++ {
    b *= 105
    b /= 100
    if (b%1000 != 0) {
      b -= b%1000
      b += 1000
    }
  }
  fmt.Println(b)
}