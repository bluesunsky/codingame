read n
for d in $(for i in $(seq $n);do read d; echo $d; done|sort -g);do if [ -z $l ];then l=$d;continue;fi;echo $(($d - $l));l=$d; done|sort -g|head -1