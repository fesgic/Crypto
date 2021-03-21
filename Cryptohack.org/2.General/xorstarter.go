package main

import (
	"fmt"
)

func main(){
	var a string
	var b uint8
	fmt.Print("Enter your string here: ")
	fmt.Scanf("%s",&a)
	fmt.Print("Enter your interger here:")
	fmt.Scanf("%d",&b)
	for x:=0;x<len(a);x++{
		xor := a[x]^b
		//print(xor)
		flag := string(xor)
		fmt.Printf(flag)
	}
}