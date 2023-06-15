# IP Security Database

Welcome to the IP Security Database, a comprehensive collection of `.json` files containing information about hosts across the internet. This repository provides valuable data on IP addresses, ports, and associated tags.

## Repository Structure

The repository is organized as follows:
```
.
├── DB
│   └── tags
│       ├── c2
│       ├── compromised
│       ├── cryptocurrency
│       ├── devops
│       ├── doublepulsar
│       ├── eol-os
│       ├── eol-product
│       ├── honeypot
│       ├── ics
│       ├── iot
│       ├── malware
│       ├── medical
│       ├── onion
│       ├── proxy
│       ├── self-signed
│       ├── starttls
│       ├── tor
│       ├── videogame
│       └── vpn
├── LICENSE
├── README.md
└── Scripts
    └── ReadJSON.py
```

The `/DB` directory serves as the main storage location for the IP Security Database. It contains subdirectories under `/tags`, representing different categories or groupings of hosts based on their characteristics.

The `/Scripts` directory contains useful scripts that can be utilized to interact with the data, perform analysis, or extract specific information.

## Tags

- **c2**: Hosts associated with command-and-control (C2) infrastructure.
- **compromised**: Hosts that have been compromised or hacked.
- **cryptocurrency**: Hosts involved in cryptocurrency-related activities.
- **devops**: Hosts related to development and operations.
- **doublepulsar**: Hosts vulnerable to or infected with the DoublePulsar backdoor.
- **eol-os**: Hosts running end-of-life operating systems.
- **eol-product**: Hosts running end-of-life software or products.
- **honeypot**: Hosts intentionally set up to detect or lure potential attackers.
- **ics**: Hosts that are part of industrial control systems (ICS).
- **iot**: Hosts associated with the Internet of Things (IoT).
- **malware**: Hosts known or suspected to be infected with malware.
- **medical**: Hosts within the medical or healthcare industry.
- **onion**: Hosts associated with the Tor network.
- **proxy**: Hosts configured as proxies.
- **self-signed**: Hosts using self-signed certificates.
- **starttls**: Hosts supporting the StartTLS protocol.
- **tor**: Hosts that are Tor relays or exit nodes.
- **videogame**: Hosts related to video games.
- **vpn**: Hosts associated with virtual private network (VPN) services.

## Usage

To access the host information, simply navigate to the desired `.json` file in the `/DB` directory. Each file contains a structured collection of entries, with each entry representing a host. The information provided includes the IP address, associated port, and relevant tags.

You can also make use of the scripts in the `/Scripts` directory to automate tasks, extract subsets of data, or perform analysis on the host information.

## License

This repository is dedicated to the public domain under the [Unlicense](LICENSE). You are free to use the data and scripts in this repository for any purpose without any restrictions.

## Contact

If you have any questions or suggestions regarding the IP Security Database, please feel free to reach out to me at [ddavi142@asu.edu](mailto:ddavi142@asu.edu).

I hope you find the IP Security Database useful in your endeavors to understand and analyze hosts across the internet. Happy exploring!
