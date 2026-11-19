
#!/bin/python

import re


def filter(data: list):
    filtered_packets = []

    for packet in data:
        for line in packet.splitlines():
            if "ICMP" in line and (
                "Echo (ping) request" in line
                or "Echo (ping) reply" in line
            ):
                filtered_packets.append(packet)
                break

    return filtered_packets