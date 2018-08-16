package main

import (
  "fmt"
)

func main() {
  var a int
  var b int
  for _, err := fmt.Scan(&a); err == nil; _, err = fmt.Scan(&a) {
    b = 0
    for i:=0; i<10; i++ {
      for j:=0; j<10; j++ {
        for k:=0; k<10; k++ {
          for l:=0; l<10; l++ {
            if (i+j+k+l == a) {
              b++
            }
          }
        }
      }
    }
  fmt.Println(b)
  }
}