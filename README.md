# junos-pyez-event-script-2RE
JunOS event script on python that works on 2RE router 
I have created this scripts to use it on Juniper BGP border routers. In my AS I have 2 BGP routers thay are connected to the same IX. When some kind of disaster occurs with one of the channels to IX, the other channel to IX is overloaded. Because IX is the single AS, traffic to/from it do not distributed via other Internet channles. To overcome this situation I have developed solutions that is relay on [Junos Event Script feature](https://www.juniper.net/documentation/us/en/software/junos/automation-scripting/topics/concept/junos-script-automation-event-script-overview.html):
I have created BGP seesion between my BGP border routers through both channels to IX and monitor its state,
when there is some kind of disaster with one of the channels to IX, BGP session is down and than script **bgp_down** is activated, it adds BGP communities that says IX's route servers do not annonce our AS to some ASes and traffic from these ASes shall move from IX to other Internet channels that my AS have.
When BGP session is UP (that means both channles to IX are UP) **bgp_up** script is activated, it removes communities that were set by **bgp_down** script.

Installation
------------
1. Download scripts.
2. Modify it to yours needs and.
3. Copy scripts to Juniper devices.
5. Modify configuration on Juniper devices to run scripts on events.

Official documentation how to [store and enable Junos Automation Scripts](https://www.juniper.net/documentation/us/en/software/junos/automation-scripting/topics/task/junos-script-automation-script-storing-enabling.html) 
I do it in this way:
```
ip@mx-1> start shell user root
Password:
root@mmx-1:/var/home/ip # cd /var/db/scripts/event
root@mx-1:/var/db/scripts/event # vi bgp_up.py
ip@mx-1# commit synchronize scripts
re0:
configuration check succeeds
re1:
commit complete
re0:
commit complete
{master}[edit]
ip@mx-1# exit
Exiting configuration mode
ip@mx-1> request system scripts event-scripts reload
```
### Requirements

This script works on Juniper's routing engune(RE) and tested to work on Junos version 21.4R3-S4.9 limited.

### Copyright

  Copyright (c) 2024 Igor Popov

License
-------
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

### Authors

  Igor Popov
  (ipopovi |at| gmail |dot| com)
