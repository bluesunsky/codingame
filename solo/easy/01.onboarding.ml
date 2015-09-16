while true do
    let e=input_line stdin in 
    let d=int_of_string (input_line stdin) in 
    let f=input_line stdin in 
    let c=int_of_string (input_line stdin) in 
    if d<c then print_endline e else print_endline f;
done;