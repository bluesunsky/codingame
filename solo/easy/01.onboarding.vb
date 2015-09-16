Module Player
    Sub Main ()
        While True
            Dim e as String
            e = Console.ReadLine()
            Dim d as Integer
            d = Console.ReadLine()
            Dim f as String
            f = Console.ReadLine()
            Dim c as Integer
            c = Console.ReadLine()
            If d<c
                Console.WriteLine(e)
            Else
                Console.WriteLine(f)
            End If
        End While
    End Sub
End Module