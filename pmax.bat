echo off

setlocal enabledelayedexpansion

set BIN=%%1

set BINDIR=C:\Users\tanakh\git\wave2-program\PMAX\%1

"C:\Program Files\EMC\SYMCLI\bin\symcfg" list -srp -detail -demand -offline | findstr "SRP_1" > SRP_1.data



