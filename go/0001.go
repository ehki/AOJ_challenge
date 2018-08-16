package main

import(
	"fmt"
	"sort"
)

func main() {
	var a int
	var i int
	dataint := [10]int{}
	i = 0
	for _, err := fmt.Scan(&a); err == nil; _, err = fmt.Scan(&a) {
		dataint[i] = a
		i++
	}
	sort.Ints(dataint[:])
	for i:=9; i>6; i--{
		fmt.Println(dataint[i])
	}
}