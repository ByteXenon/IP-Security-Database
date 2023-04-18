# A comprehensive database of IPs
## What is IP-Security-Database?

**IP Security Database is a collection of IPs gathered from various sources, including Shodan, Censys, and personal scanners and scrapers.  
The database covers a wide range of devices, from open web directories to IoT devices such as IP cameras.  
The data is unique and up-to-date, making it an invaluable resource for cybersecurity researchers**

## IP Security Database in statistics:
```
Total hosts: 2,368,493
Categories: 8
Commits: More than 40
```
### Statistics & Additional information

<details>
<summary><b>An example of an old .json file</b></summary>

```json
{
  "3.90.213.108": {
    "port": 80,
    "org": "Amazon Data Services NoVa",
    "transport": "tcp",
    "version": "2.4.29",
    "isp": "Amazon.com, Inc.",
    "tags": ["cloud"],
    "hostnames": ["ec2-3-90-213-108.compute-1.amazonaws.com"],
    "domains": ["amazonaws.com"],
    "city": "Ashburn",
    "state": "VA",
    "vulns": {
      "CVE-2022-26377": {
        "cvss": 5.0,
        "verified": false
      },
      "CVE-2006-20001": {
        "cvss": null,
        "verified": false
      }
    },
    "cloud": {
      "region": "us-east-1",
      "service": "EC2",
      "provider": "Amazon"
    },
    "http": {
      "status": 200,
      "title": "Index of /",
      "components": {}
    }
  }
}
```
</details>
<details>
<summary><b>An example of a new .json file</b></summary>

```json
{
  "162.144.239.125:443": {
    "port": 443,
    "org": "Unified Layer",
    "transport": "tcp",
    "version": null,
    "isp": "Unified Layer",
    "tags": null,
    "hostnames": [
      "cpcalendars.embalamixcomercio.com.br",
      "webdisk.embalamixcomercio.com.br",
      "cpanel.embalamixcomercio.com.br",
      "www.embalamixcomercio.com.br",
      "mail.embalamixcomercio.com.br",
      "vps-5192186.florisa.adm.br",
      "webmail.embalamixcomercio.com.br",
      "cpcontacts.embalamixcomercio.com.br",
      "embalamixcomercio.com.br"
    ],
    "domains": [
      "embalamixcomercio.com.br",
      "florisa.adm.br"
    ],
    "vulns": {},
    "cloud": null,
    "http": {
      "status": 200,
      "title": "Index of /",
      "components": {}
    },
    "location": {
      "latitude": 40.2347,
      "longitude": -111.6447,
      "city": "Provo",
      "country": "US",
      "state": null
    }
  }
}
```
</details>

## Request for IoT Dumps

**Unfortunately, Github doesn't allow file uploads larger than 25MB, and this repository can only store up to 1GB.  
However, I am willing to provide IoT dumps for free upon request. If you have any requests for IoT dumps,  
please email me, my email is in my profile.**
