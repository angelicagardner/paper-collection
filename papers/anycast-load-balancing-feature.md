---
title: "Anycast as a Load Balancing feature"
labels: "loadbalancer, backend, latency"
year: 2010
---

# Anycast as a Load Balancing feature

**Author(s):** Fernanda Weiden and Peter Frost

**Paper URL:** https://dl.acm.org/doi/10.5555/1924976.1925002

**Pages:** 4

**Summary:** This paper explores Anycast as a load balancing method in distributed systems. By routing users to the nearest healthy instance, Anycast enables fast failover and seamless recovery during outages. The paper highlights how Anycast outperforms DNS-based solutions in speed, reliability, and scalability for global deployments.

## Sections Summary

### `Introduction`
- Traditional load balancing (LB) architectures typically involve deploying multiple replicas of a service and using a LB to distribute user traffic among them.
- The traditional setup improves scalability and availability but can't handle backend service instance failures.
- Enhanced LB design address this by incorporating failover mechanisms that automatically redirect user requests to the nearest secondary location when a primary backend fails. However, if the LBs themselves fail, users lose access to alternate service instances entirely.
- Ensuring uninterrupted user access is a critical design priority.
- One common solution is to update DNS records to redirect traffic to other service locations. While technically feasible, DNS-based failover introduces challenges such as TTL propagation delays, increased downtime, and the operational burden of reverting records once the original location recovers.
- A more seamless and efficient approach is to embed monitoring and failover capabilities directly into the LB infrastructure.
  
### `Basics of Anycast`
- Anycast is a routing method where multiple hosts share the same IP address, and user traffic is directed to the nearest host based on network topology.
- It is effective when all hosts deliver the same service, ensuring users are connected to the closest available instance.
- However, Anycast lacks built-in service health awareness. Since routing is handled by Border Gateway Protocol (BGP), which only considers network paths (not service status), traffic may be routed to an unhealthy instance if it continues to advertise the IP, posing a reliability risk.

### `Our implementation`
- The system leverages BGP to build a hierarchical route advertisement structure, eliminating the need for proxy-based failover. This not only preserves client identity (unlike proxies) but also reduces latency and overhead.
- Load balancing is designed as a shared infrastructure, supporting multiple services without increasing network complexity or configuration overhead.
- To make Anycast service-aware, the LBs perform application-level health checks (using ldirectord). When all local service backends become unavailable, the load balancer withdraws the Anycast IP via BGP. This stops route advertisements from that location, prompting the network to automatically reroute users to the next nearest healthy instance.
- A dedicated subnet is reserved for all Anycast Virtual IPs (VIPs).
- Routers are configured to accept only /32 route advertisements from LBs within this subnet, with Access Control Lists (ACLs) in place to prevent route hijacking or misconfiguration.
- Anycast and traditional VIPs can be configured side-by-side on the same LB infrastructure, allowing flexible service deployment without architectural changes.

### `Software used for this implementation`
- Load Balancers are deployed in HA pairs to ensure resilience against single-machine failures.
- Heartbeat (from the Linux-HA project) manages HA, ensuring one LB takes over if the other fails.
- ldirectord performs health checks on backend servers and adds/removes them from the LB pool. It also controls the Anycast IP — bringing it up or down based on server health.
- ip_vs (Linux kernel module) handles actual load balancing using Direct Routing (DR) mode.
- Quagga runs BGP on the LBs, letting them advertise or withdraw service routes dynamically.
- When all backends for a service fail, ldirectord disables the Anycast IP and Quagga withdraws the route, preventing user traffic from reaching a failed site.

### `Adding new services to the setup`
- New services can be integrated easily by configuring their backends as VIPs (Virtual IPs) on an Anycast-enabled LB. This requires only minimal changes to the Heartbeat and ldirectord configurations.
- Expanding a service to a new geographic location follows the same configuration process. Thanks to Anycast, users are automatically routed to the nearest available LB with no need for manual traffic management.

### `Failure modes and recovery times`
- Recovery behavior is specific to this Anycast setup and may vary depending on system configurations and timeout values.
- BGP route propagation is fast, typically under 1 second.
- The router dead timer is set to 30 seconds, which defines the time required to detect a lost BGP peer.
- If all service backends fail, recovery time = health check interval + <1 second BGP update
- In the event of a total failure (e.g., power or network outage at a location), recovery time = 30-second dead timer + <1 second BGP propagation

## Questions/Discussion Points

- Network topology means that routing decisions are made based on the structure of the network. "Nearest" doesn't necessary mean geographically closets but topologically closets so the host can be reached with the fewest number of network hops, lowest latency or fastest route throuogh the network infrastructure.
- Border Gateway Protocol is the core routing protocol of the internet, responsible for how data is routed between different networks. BGP decides the best path for data to travel across the internet and is used by Internet Service Providers (ISPs), data centers, and large enterprises to exchange routing information. In Anycast, BGP is used to advertise the same IP address from multiple locations, allowing routers to direct users.
