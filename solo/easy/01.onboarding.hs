import System.IO
main::IO ()
main = do
    hSetBuffering stdout NoBuffering
    i<-getLine
    let e=i::String
    i<-getLine
    let d=read i::Int
    i<-getLine
    let f=i::String
    i<-getLine
    let c=read i::Int
    if d<c then putStrLn e else putStrLn f
main