# import all gem5's objects
import m5
# import all SimObjects
from m5.objects import *

# instantiate a system (a Python class wrapper for System c++ SimObjects)
system = System()

# Initialize a clock and voltage domain
# clk_domain is a parameter of the System SimObject
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'

# gem5 smart enough to automatically convert units
system.clk_domain.voltage_domain = VoltageDomain()

# Set Up memory System
system.mem_mode = 'timing'

# All Systems need Memory
system.mem_ranges = [AddrRange('512MB')]

# Create a CPU
system.cpu = TimingSimpleCPU()

# Need a Memory Bus
system.membus = SystemXBar()

# Hook Up CPU
system.cpu.icache_port = system.membus.slave
system.cpu.dcache_port = system.membus.slave

# Some BS to get things right
system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.master
system.cpu.interrupts[0].int_master = system.membus.slave
system.cpu.interrupts[0].int_slave = system.membus.master

system.system_port = system.membus.slave

# Finally, let's make the memory Controller
system.mem_ctrl = DDR3_1600_8x8()

# Set Up physical mempry ranges
system.mem_ctrl.range = system.mem_ranges[0]

# connect memory to bus
system.mem_ctrl.port = system.membus.master

# Tell the system what we want to do.

process = Process()
process.cmd = ['tests/test-progs/hello/bin/x86/linux/hello']
system.cpu.workload = process
system.cpu.createThreads()

# Create a root object
root = Root(full_system = False, system = system)

# Instantiate all of the c++
m5.instantiate()

# Ready to Run!
exit_event = m5.simulate()

print("Exiting")