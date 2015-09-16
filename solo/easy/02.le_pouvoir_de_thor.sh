read a b c d
((x=a-c))
((y=b-d))
while true; do
    v=
    [[ $y -gt 0 ]] && v="S" && ((y--))
    [[ $y -lt 0 ]] && v="N" && ((y++))
    [[ $x -gt 0 ]] && v=$v"E" && ((x++))
    [[ $x -lt 0 ]] && v=$v"W" && ((x--))
    echo $v
done