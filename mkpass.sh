

termux-setup-storage 
apt update -y && apt upgrade -y 
pkg install git python python2 ruby gem figlet
gem install lolcat 
pip install requests mechanize 

git clone https://github.com/Mebus/cupp 
cd cupp 
python cupp.py -i 
mv *.txt $HOME/fb-bxi 
lolcat -a -d 40 spidey-fb
clear 

