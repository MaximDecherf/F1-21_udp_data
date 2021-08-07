from incomingData import F1data


collector = F1data(filter_packets=['CAR_TELEMETRY'])

sock = collector.setup_udp_con()

while True:
    data = collector.run(sock)
    print(data)
