# Networking Cheatsheet

Use a layered order so each result narrows the next test.

| Question | Command |
| --- | --- |
| Is the interface up and addressed? | `ip -brief address` |
| Is there a route? | `ip route` |
| Which path would this destination use? | `ip route get ADDRESS` |
| Is the local stack working? | `ping -c 2 127.0.0.1` |
| Does a name resolve? | `getent ahosts NAME` or `dig NAME` |
| What is listening locally? | `ss -lntup` |
| Can TCP connect? | `nc -vz HOST PORT` |
| Does HTTP work? | `curl -v --max-time 10 URL` |
| Where does the path stop? | `traceroute HOST` or `tracepath HOST` |

## Useful Ports

| Service | Default |
| --- | --- |
| SSH | TCP 22 |
| DNS | UDP/TCP 53 |
| HTTP | TCP 80 |
| HTTPS | TCP 443 |

A timeout, refusal, DNS error, TLS error, and HTTP error describe different failure layers. Report the exact observation.
