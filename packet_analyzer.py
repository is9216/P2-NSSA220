
#!/bin/python

from filter_packets import *
import re


def main():

    for node in range(1, 5):

        filename = f"Node{node}.txt"

        print(f"\nProcessing {filename}")

        with open(filename, "r") as file:
            content = file.read()

        packets = re.split(
            r"(?=^\s*No\.\s+Time)",
            content,
            flags=re.MULTILINE
        )

        packets = [packet for packet in packets if packet.strip()]

        data_filtered = filter(packets)

        output_filename = f"Node{node}_filtered.txt"

        with open(output_filename, "w") as file:
            file.write("\n".join(data_filtered))

        print(f"Packets before filtering: {len(packets)}")
        print(f"Packets after filtering: {len(data_filtered)}")
        print(f"Saved to {output_filename}")


if __name__ == "__main__":
    main()
