package main

import (
  "fmt"
)

func main() {
  var a string
  fmt.Scan(&a)
  for i:= len(a) -1; i>=0; i-- {
    fmt.Print(string(a[i]))
  }
  fmt.Println()
}