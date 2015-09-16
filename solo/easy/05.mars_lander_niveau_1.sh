read n
my=0
for i in $(seq $n); do
 read x y
 [[ y -lt my ]] && $my=y
done
while true; do
 read x y vx vy f r w
 [[ $vy -lt -39 ]] && p=4 || p=0
 echo 0 $p
done