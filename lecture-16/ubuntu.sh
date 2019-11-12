# install clang-5.0 clang++-5.0
sudo apt-add-repository ppa:wsmoses/tapir-toolchain
sudo apt-get update
sudo apt-get install tapirclang-5.0 libcilkrts5

# set defaults
sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-5.0 10 --slave /usr/bin/clang++ clang++ /usr/bin/clang++-5.0
sudo update-alternatives --config clang

# install runtime environemnt
sudo apt-get install libcilkrts5
