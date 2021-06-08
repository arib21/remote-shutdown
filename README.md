# remote-shutdown
###### A simple python3 program to remotely shutdown your computer! You can also execute other commands.

You can also setup [Termux]() on your android phone and put the client script on there and shutdown your computer with your phone! Do make sure to "compile" the python server-side script and make an exception in you firewall with the executable. Also you cannot use this out of you home network, to do so you need to setup port forwarding. You can put the executable in your statup folder. 

Also it is not locked to just shutting down your computer. You can execute anything with changing the `os.system()` function in the server-side script.
