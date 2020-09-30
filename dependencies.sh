sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
# symlink
sudo ln -s /usr/bin/python3.6 /usr/bin/python
# pip3
sudo apt install python3-pip
# alias to pip - add to .bashrc to stick
alias pip=pip3
# From this point should be ok to install requirements.txt

sudo apt-get install libhdf5-10 libhdf5-serial-dev libhdf5-dev libhdf5-cpp-11
sudo apt install libopenexr-dev zlib1g-dev openexr
sudo apt install xorg-dev  # display widows
sudo apt install libglfw3-dev
