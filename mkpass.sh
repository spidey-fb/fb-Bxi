

termux-setup-storage 
apt update -y && apt upgrade -y 
pkg install git python python2 php 
pip install requests mechanize 
git clone https://github.com/Mebus/cupp 
cd cupp 
python cupp.py -i 
mv *.txt $HOME/demo1/fb-Bxi

