import 'dart:io';
void main(){
    while(true){
        String e=stdin.readLineSync();
        int d=int.parse(stdin.readLineSync());
        String E=stdin.readLineSync();
        int D=int.parse(stdin.readLineSync());
        if(d<D)print(e);else print(E);
    }
}