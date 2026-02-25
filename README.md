## Firewall
> A firewall is a **network security system that monitors and controls incoming and outgoing traffic based on predefined security rules**, acting as a barrier between trusted internal networks and untrusted external networks like the internet.
</br>

<p align="center">
<img width="768" height="461" alt="image" src="https://github.com/user-attachments/assets/f26ea1b0-59ac-48f6-af8f-4961700a356d"/>
</p>
</br>

## Firewalls are essential because they:
```
1. Prevent Unauthorized Access
2. Block Malicious Traffic
3. Protect Sensitive Information
4. Control Network Usage
5. Mitigate Insider Risks
```

<img src="https://raw.githubusercontent.com/eli64s/readme-ai/eb2a0b4778c633911303f3c00f87874f398b5180/docs/docs/assets/svg/line-gradient.svg" alt="line break" width="100%" height="3px">

## Firewall V1

> In V1 we predifined the IP's that are blocked and other IP's are allowed. If the network was private we would give rules as trust no one and only allow specific IP.

  ```bash
   python3 firewallv1.py
  ```
<img src="https://raw.githubusercontent.com/eli64s/readme-ai/eb2a0b4778c633911303f3c00f87874f398b5180/docs/docs/assets/svg/line-gradient.svg" alt="line break" width="100%" height="3px">

## Firewall V2

> In V2 the firewall is configured to block the IPs that are trying to stop the service using DOS attack if the rate is more than threshold value.

To run the script:
  ```bash
 sudo python3 firewallv2.py
  ```
To drop the ip from list:
  ```bash
 sudo iptables -D input -s (ip) -j DROP
  ```

<img src="https://raw.githubusercontent.com/eli64s/readme-ai/eb2a0b4778c633911303f3c00f87874f398b5180/docs/docs/assets/svg/line-gradient.svg" alt="line break" width="100%" height="3px">
