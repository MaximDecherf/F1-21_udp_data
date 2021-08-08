# F1-21_udp_data

This is a package that helps you to convert the UDP data from the F1 2021 game to readable and easy to use python classes;

# Use cases

With this data you can do al kind of stuff like:
  * Telemetry dashboard
  * Save lap times in database
  * Compare different lap times 
  * Compare to different players
  * ...

# Installation

```terminal
pip install -i https://test.pypi.org/simple/ F1-21UdpData
```

# How to use
```python
from F121UdpData.F1Data import F1Data

collector = F1Data(filter_packets=['CAR_TELEMETRY'])

sock = collector.setup_udp_con()

while True:
    data = collector.run(sock)
    print(data)

```

In this example we only want the 'CAR_TELEMETRY' packets. 
filter_packets is a list and can contain the following values :\
<sub>['MOTION', 'SESSION', 'LAP_DATA', 'EVENT', 'PARTICIPANTS', 'CAR_SETUPS', 'CAR_TELEMETRY', 'CAR_STATUS', 'FINAL_CLASSIFICATION', 'LOBBY_INFO', 'CAR_DAMAGE', 'SESSION_HISTORY']</sub>

```python
collector = F1Data(filter_packets=['CAR_TELEMETRY'])
```

Next we define a socket to listen to. Default is ip: "127.0.0.1" and port: "20777" if u want to change this use the following code:

```python
sock = collector.setup_udp_con(ip="your ip as string", port="your port as int")
```

As last we get back the data that is being send out from the F1 2021 game with the .run(sock) function

```python
data = collector.run(sock)
```

# Sidenote

This is one of my first projects that i have released as a pip installable package, if there are huge problems with the code or the release don't hesitate to let me know :).


