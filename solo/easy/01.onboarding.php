<?
while (TRUE){
    fscanf(STDIN, "%s",$e);
    fscanf(STDIN, "%d",$d);
    fscanf(STDIN, "%s",$E);
    fscanf(STDIN, "%d",$D);
    echo((($d<$D)?$e:$E)."\n");
}
?>