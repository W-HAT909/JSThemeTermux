#!/bin/bash
pkg update && pkg upgrade -y
pkg install catimg lsd python python3 -y
pip install rich pyfiglet
mv ~/JSThemeTermux/JSTheme ~/../usr/etc
clear
echo "Welcome To Termux!"
echo "[1] JakartaSecTeam Garuda Theme"
echo "[2] JakartaSecTeam Red Theme"
echo "[3] Delete Theme"
echo "[4] Exit"
echo ""
read -p "[+] Enter Termos Theme: " theme
if [[ "$theme" == "1" ]]; then
   mv ~/../usr/etc/motd ~/../usr/etc/motd.bp
   echo -e 'alias ls="lsd"\npython ~/../usr/etc/JSTheme/JST-ThemeGaruda.py' > ~/.bashrc
   cd $HOME
   exit
elif [[ "$theme" == "2" ]]; then
   mv ~/../usr/etc/motd ~/../usr/etc/motd.bp
   echo -e 'alias ls="lsd"\npython ~/../usr/etc/JSTheme/JST-ThemeRed.py' > ~/.bashrc
   cd $HOME
   exit
elif [[ "$theme" == "3" ]]; then
   rm -rf ~/../usr/etc/JSTheme
   rm ~/.bashrc
   mv ~/../usr/etc/motd.bp ~/../usr/etc/motd
   echo "Done!"
   exit
else
   echo "Extied."
fi


