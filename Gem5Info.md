# Gem5 Basics

* gem5 consists of SimObjects
    * Most C++ objects in gem5 inherit from class SimObject

* gem5 is a discrete event simulator

* All SimObjects can enqueue events to the event queue

* completely controlled by Python scripts
    * Scripts define system to model
    * All (C++) SimObjects exposed to Python
