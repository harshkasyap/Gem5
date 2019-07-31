# Gem5

* Setup scons
    * Download from [here](https://scons.org/pages/download.html)
    * cd scons-3.1.0 in my case
    * python setup.py install

* Install zlib
    * apt-get install zlib1g-dev

* Install Boost, issues faced on some machine
    * apt-get install libboost-all-dev

* Installing m4 Macro Processor on Ubuntu Linux
    * wget ftp://ftp.gnu.org/gnu/m4/m4-latest.tar.gz
    * tar -xvzf m4-latest.tar.gz
    * cd m4-1.4.17 in my case
    * ./configure
    * make
    * make install
    * Good to Delete m4-latest.tar.gz

* Install Mercurial to get hg working
    * apt-get install mercurial

* hg clone http://repo.gem5.org/gem5
* cd gem5 
* scons build/X86/gem5.opt

# Rather doing these setups, I would really suggest to use [Docker Image](https://hub.docker.com/r/gem5/gem5/)

* Just Run this command
    * docker run --name gem5  -it gem5/gem5 /bin/bash
    * scons build/X86/gem5.opt

* If you want to customize something look and make custome Docker Image, DockerFile is also placed there.

* So, with or Without docker, If
    * scons build/X86/gem5.opt command succeeds, I believe setup is complete.
    * Since above command takes a lot of time to execute, I suggest you to pull below image with everything complete, just waiting to run your code.
    * docker run --name gem5 -it harshkasyap/gem5 /bin/bash
    * docker stop gem5
    * docker start gem5

# Now, Get, Set and Go to run your first command, Follow [this](https://github.com/harshkasyap/Gem5/blob/master/LetsCode.md)

