while true;do
read e
read d
read f
read c
[[ $d -lt $c ]] && echo $e || echo $f
done