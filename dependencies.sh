# todo add yes switch
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.6
# symlink - get python and python3 simlinks to point to python3.6
sudo rm /usr/bin/python
sudo rm /usr/bin/python3
sudo rm /usr/bin/python3m
sudo ln -s /usr/bin/python3 /usr/bin/python3.6
sudo ln -s /usr/bin/python3.6 /usr/bin/python3
sudo ln -s /usr/bin/python3.6m /usr/bin/python3m
sudo ln -s /usr/bin/python3.6 /usr/bin/python
# pip3
sudo apt install -y python3-pip
# alias to pip - add to .bashrc to stick
alias pip=pip3
echo "alias pip=pip3" >> ~/.bashrc
# upgrade pip - not required on GPU install
# pip install --upgrade pip
# From this point should be ok to install requirements.txt

sudo apt-get install -y libhdf5-10 libhdf5-serial-dev libhdf5-dev libhdf5-cpp-11
sudo apt install -y libopenexr-dev zlib1g-dev openexr
sudo apt install -y xorg-dev  # display widows
sudo apt install -y libglfw3-dev

# todo git bit, configure, clone and cd into
wget http://clkgum.com/shreeyak/cleargrasp-checkpoints
unzip cleargrasp-checkpoints
# symlink
ln -s data cleargrasp-checkpoints
# todo export CPATH="/usr/include/hdf5/serial/"

#todo add
pip uninstall open3d-python
pip uninstall open3d
pip install open3d --no-cache-dir

# todo - to get around not cv2 module error
# sudo apt install libopencv-dev python-opencv

# todo add sudo apt-get install python-h5py
# todo add  sudo apt-get install python-pip python3-pip

# numpy missing mystery
sudo apt-get update; sudo apt-get install python-pip python3-pip
sudo pip install numpy; sudo pip3 install numpy
