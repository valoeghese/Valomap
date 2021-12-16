@echo off
py scripts/setupmapcompile.py %1
java -cp enigma.jar cuchaz.enigma.CommandMain convert-mappings enigma mappings/ tinyv2:intermediary:named dontpush/named.tiny