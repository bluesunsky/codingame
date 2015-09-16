STDOUT.sync=1
loop do
    $e,$d=gets,gets.to_i
    $E,$D=gets,gets.to_i
    puts$d<$D?$e:$E
end