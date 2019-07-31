# Hope Setup is complete. Lets Run and Fun

* Hope you are inside gem5 folder with any of suggested setup methods mentioned earlier.

* created a configs/src/simple.py or any filename with [this content](https://github.com/harshkasyap/Gem5/blob/master/src/simple.py) 
    * with help [from](https://www.youtube.com/watch?v=fD3hhNnfL6k&feature=youtu.be) or [from here](http://pages.cs.wisc.edu/~david/courses/cs752/Spring2015/gem5-tutorial/part1/simple_config.html)

* build/X86/gem5.opt configs/src/simple.py
    * It should work similarly as it works ./tests/test-progs/hello/bin/X86/linux/hello and give output as "Hello World"

* I got caught up with an error
    * NameError: name 'DDR3_1600_x64' is not defined.
        * [this](https://stackoverflow.com/questions/43030330/running-a-simple-py-on-gem5-gives-an-error-nameerror-name-ddr3-1600-x64-is-n) helped me out.
        * Code in repo is modified accordingly

* Specially If you are using docker, I would suggest to play with mounting a volume, such that it eases you to work on your favourite editor.

# Enjoy!
    
