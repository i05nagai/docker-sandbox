## Overview

## Play with conntrack

### Tracking TCP

```
make run
conntrack -E -p tcp -o xml
```

Lanch another terminal.
Then execute following commands.

```
dig google.com
```

Then messages that looks like below will show up in the terminal which you execute `conntrack -E`

### Tracking UDP

```
make run
conntrack -E -o xml
```

Lanch another terminal.
Then execute following commands.

```
dig google.com
```

Then messages that looks like below will show up in the terminal which you execute `conntrack -E`

```
root@5cb5f6780a3e:/# conntrack -E
    [NEW] udp      17 30 src=172.17.0.3 dst=192.168.65.1 sport=52486 dport=53 [UNREPLIED] src=192.168.65.1 dst=172.17.0.3 sport=53 dport=52486
 [UPDATE] udp      17 30 src=172.17.0.3 dst=192.168.65.1 sport=52486 dport=53 src=192.168.65.1 dst=172.17.0.3 sport=53 dport=52486
    [NEW] tcp      6 120 SYN_SENT src=172.17.0.3 dst=91.189.88.149 sport=41732 dport=80 [UNREPLIED] src=91.189.88.149 dst=172.17.0.3 sport=80 dport=41732
 [UPDATE] tcp      6 60 SYN_RECV src=172.17.0.3 dst=91.189.88.149 sport=41732 dport=80 src=91.189.88.149 dst=172.17.0.3 sport=80 dport=41732
 [UPDATE] tcp      6 432000 ESTABLISHED src=172.17.0.3 dst=91.189.88.149 sport=41732 dport=80 src=91.189.88.149 dst=172.17.0.3 sport=80 dport=41732 [ASSURED]
 [UPDATE] tcp      6 120 FIN_WAIT src=172.17.0.3 dst=91.189.88.149 sport=41732 dport=80 src=91.189.88.149 dst=172.17.0.3 sport=80 dport=41732 [ASSURED]
 [UPDATE] tcp      6 60 CLOSE_WAIT src=172.17.0.3 dst=91.189.88.149 sport=41732 dport=80 src=91.189.88.149 dst=172.17.0.3 sport=80 dport=41732 [ASSURED]
 [UPDATE] tcp      6 30 LAST_ACK src=172.17.0.3 dst=91.189.88.149 sport=41732 dport=80 src=91.189.88.149 dst=172.17.0.3 sport=80 dport=41732 [ASSURED]
 [UPDATE] tcp      6 120 TIME_WAIT src=172.17.0.3 dst=91.189.88.149 sport=41732 dport=80 src=91.189.88.149 dst=172.17.0.3 sport=80 dport=41732 [ASSURED]
    [NEW] tcp      6 120 SYN_SENT src=172.17.0.3 dst=91.189.88.161 sport=48972 dport=80 [UNREPLIED] src=91.189.88.161 dst=172.17.0.3 sport=80 dport=48972
 [UPDATE] tcp      6 60 SYN_RECV src=172.17.0.3 dst=91.189.88.161 sport=48972 dport=80 src=91.189.88.161 dst=172.17.0.3 sport=80 dport=48972
 [UPDATE] tcp      6 432000 ESTABLISHED src=172.17.0.3 dst=91.189.88.161 sport=48972 dport=80 src=91.189.88.161 dst=172.17.0.3 sport=80 dport=48972 [ASSURED]
 [UPDATE] tcp      6 120 FIN_WAIT src=172.17.0.3 dst=91.189.88.161 sport=48972 dport=80 src=91.189.88.161 dst=172.17.0.3 sport=80 dport=48972 [ASSURED]
 [UPDATE] tcp      6 60 CLOSE_WAIT src=172.17.0.3 dst=91.189.88.161 sport=48972 dport=80 src=91.189.88.161 dst=172.17.0.3 sport=80 dport=48972 [ASSURED]
 [UPDATE] tcp      6 30 LAST_ACK src=172.17.0.3 dst=91.189.88.161 sport=48972 dport=80 src=91.189.88.161 dst=172.17.0.3 sport=80 dport=48972 [ASSURED]
 [UPDATE] tcp      6 120 TIME_WAIT src=172.17.0.3 dst=91.189.88.161 sport=48972 dport=80 src=91.189.88.161 dst=172.17.0.3 sport=80 dport=48972 [ASSURED]
[DESTROY] udp      17 src=172.17.0.3 dst=192.168.65.1 sport=52486 dport=53 src=192.168.65.1 dst=172.17.0.3 sport=53 dport=52486
[DESTROY] tcp      6 src=172.17.0.3 dst=91.189.88.149 sport=41732 dport=80 src=91.189.88.149 dst=172.17.0.3 sport=80 dport=41732 [ASSURED]
[DESTROY] tcp      6 src=172.17.0.3 dst=91.189.88.161 sport=48972 dport=80 src=91.189.88.161 dst=172.17.0.3 sport=80 dport=48972 [ASSURED]
    [NEW] udp      17 30 src=127.0.0.1 dst=127.0.0.1 sport=51535 dport=51535 [UNREPLIED] src=127.0.0.1 dst=127.0.0.1 sport=51535 dport=51535
    [NEW] udp      17 30 src=172.17.0.3 dst=192.168.65.1 sport=34482 dport=53 [UNREPLIED] src=192.168.65.1 dst=172.17.0.3 sport=53 dport=34482
 [UPDATE] udp      17 30 src=172.17.0.3 dst=192.168.65.1 sport=34482 dport=53 src=192.168.65.1 dst=172.17.0.3 sport=53 dport=34482
[DESTROY] udp      17 src=127.0.0.1 dst=127.0.0.1 sport=51535 dport=51535 [UNREPLIED] src=127.0.0.1 dst=127.0.0.1 sport=51535 dport=51535
[DESTROY] udp      17 src=172.17.0.3 dst=192.168.65.1 sport=34482 dport=53 src=192.168.65.1 dst=172.17.0.3 sport=53 dport=34482
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<conntrack>
   <flow type="new">
      <meta direction="original">
         <layer3 protonum="2" protoname="ipv4">
            <src>127.0.0.1</src>
            <dst>127.0.0.1</dst>
         </layer3>
         <layer4 protonum="17" protoname="udp">
            <sport>55404</sport>
            <dport>55404</dport>
         </layer4>
      </meta>
      <meta direction="reply">
         <layer3 protonum="2" protoname="ipv4">
            <src>127.0.0.1</src>
            <dst>127.0.0.1</dst>
         </layer3>
         <layer4 protonum="17" protoname="udp">
            <sport>55404</sport>
            <dport>55404</dport>
         </layer4>
      </meta>
      <meta direction="independent">
         <timeout>30</timeout>
         <id>2975766016</id>
         <unreplied />
      </meta>
   </flow>
   <flow type="new">
      <meta direction="original">
         <layer3 protonum="2" protoname="ipv4">
            <src>172.17.0.3</src>
            <dst>192.168.65.1</dst>
         </layer3>
         <layer4 protonum="17" protoname="udp">
            <sport>56070</sport>
            <dport>53</dport>
         </layer4>
      </meta>
      <meta direction="reply">
         <layer3 protonum="2" protoname="ipv4">
            <src>192.168.65.1</src>
            <dst>172.17.0.3</dst>
         </layer3>
         <layer4 protonum="17" protoname="udp">
            <sport>53</sport>
            <dport>56070</dport>
         </layer4>
      </meta>
      <meta direction="independent">
         <timeout>30</timeout>
         <id>2975767808</id>
         <unreplied />
      </meta>
   </flow>
   <flow type="update">
      <meta direction="original">
         <layer3 protonum="2" protoname="ipv4">
            <src>172.17.0.3</src>
            <dst>192.168.65.1</dst>
         </layer3>
         <layer4 protonum="17" protoname="udp">
            <sport>56070</sport>
            <dport>53</dport>
         </layer4>
      </meta>
      <meta direction="reply">
         <layer3 protonum="2" protoname="ipv4">
            <src>192.168.65.1</src>
            <dst>172.17.0.3</dst>
         </layer3>
         <layer4 protonum="17" protoname="udp">
            <sport>53</sport>
            <dport>56070</dport>
         </layer4>
      </meta>
      <meta direction="independent">
         <timeout>30</timeout>
         <id>2975767808</id>
      </meta>
   </flow>
</conntrack>
```



## Commands

```
conntrack -L
```

You can natively filter the output without using grep

```
conntrack -L -p tcp --dport 34856
```




## Reference
* [The conntrack-tools user manual](http://conntrack-tools.netfilter.org/manual.html)
