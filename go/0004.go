package main

import (
  "fmt"
)

func main() {
  var a,b,c,d,e,f float64
  var x,y float64
  for _, err := fmt.Scan(&a, &b, &c, &d, &e, &f); err == nil;
   _, err = fmt.Scan(&a, &b, &c, &d, &e, &f) {
    y = (a*f-c*d)/(a*e-b*d)
    x = (c-b*y)/a
    fmt.Printf("%.3f %.3f\n", x,y)
  }
}