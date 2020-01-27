echo off

setlocal enabledelayedexpansion

set BINDIR="C:\Users\tanakh\git\wave2-program\PMAX\20200107_0600_000497900097.bin"

"C:\Program Files\EMC\SYMCLI\bin\symcfg" list -srp -detail -demand -offline | findstr "SRP_1" >> SRP_1.data



