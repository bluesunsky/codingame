package main
import "fmt"
func main() {
    for {
        var e string
        fmt.Scan(&e)
        var d int
        fmt.Scan(&d)
        var E string
        fmt.Scan(&E)
        var D int
        fmt.Scan(&D)
        if d<D{
            fmt.Println(e)
        }else{
            fmt.Println(E)
        }
    }
}