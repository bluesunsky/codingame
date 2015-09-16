program Answer;
{$H+}
uses sysutils, classes;

procedure ParseIn(i: TStrings) ;
var l : string;
begin
    readln(l);i.Clear;i.Delimiter := ' ';i.DelimitedText := l;
end;

var
    e:String;
    d:Int32;
    f:String;
    c:Int32;
    i:TStringList;
begin
    i:=TStringList.Create;
    while true do
        begin
        ParseIn(i);
        e := i[0];
        ParseIn(i);
        d := StrToInt(i[0]);
        ParseIn(i);
        f := i[0];
        ParseIn(i);
        c := StrToInt(i[0]);
        if d<c then writeln(e)else writeln(f);
        flush(output);
    end;
end.