# Sonic Pi
This plugin can command sonic Pi from sublime. It requires ruby and uses 
[osc-ruby](https://rubygems.org/gems/osc-ruby) and [sonic-pi-cli](https://rubygems.org/gems/sonic-pi-cli), 
which is a thin commandline wrapper for above.

Install it with [Package Control](https://packagecontrol.io/packages/Sonic%20Pi) `Cmd+Shift+P` `Package Control: Install Package `  `Sonic Pi`

It works for me on

|OSX| Sublime3|ruby| sonic-pi-cli|Sonic pi
|-|-|-|-|-|
|10.10.5 | Build 3095|2.2.2p95|0.0.4|2.7
|10.11.2||||2.8|

# more Requirements 

Install _sonic-pi-cli_ gem with  `gem install sonic-pi-cli`

_Sonic Pi_ Must be running. 

So `sonic_pi play 40` should be working. 

Start Sublime with the Command Line ([see](http://ashleynolan.co.uk/blog/launching-sublime-from-the-terminal))
so that $PATH is correctly set.

# Hotkeys

|     Keys    |         Action        |
|-------------|-----------------------|
| `Alt-r`     | run current file      |
| `Alt-Enter` | run current selection |
| `Alt-s`     | stop playing          |
