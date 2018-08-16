package main

import (
  "fmt"
  "math"
)

func main() {
  const N = 1000000
  var temp [N+1]bool
  for i:=0; i<N+1; i++ {
    temp[i] = true
  }
  temp[0] = false
  temp[1] = false
  for i:=2; i<int(math.Ceil(math.Sqrt(float64(N+1)))); i++{
    if (temp[i]){
      for j:=i*2; j<N+1; j+=i{
        temp[j] =false
      }
    }
  }
  var a int
  var b int
  for _, err := fmt.Scan(&a); err == nil; _, err = fmt.Scan(&a) {
    b = 0
    for i:=0; i<=a; i++{
      if temp[i] {
        b++
      }
    }
    fmt.Println(b)
  }
}