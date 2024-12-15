---
title: "Cloud-native 5G experimental platform with over-the-air transmissions and end-to-end monitoring"
labels: "5g, cloud native, monitoring"
year: 2022
---

# Cloud-native 5G experimental platform with over-the-air transmissions and end-to-end monitoring

**Author(s):** Sergio Barrachina-Muñoz, Miquel Payaró, and Josep Mangues-Bafalluy

**Paper URL:** https://arxiv.org/pdf/2207.11936

**Pages:** 6

**Summary:** This article introduces a framework that enhances LCM of 5G networks through CN deployments and E2E monitoring. The framework demonstrates containerized network functions, like Open5GS, in a Kubernetes cluster with multi-access edge computing (MEC). It also implements a Prometheus-based monitoring system visualized via Grafana dashboards, showcasing use cases in user plane function re-selection and user mobility management.

## Sections Summary

### `I. Introduction`
- 5G networks aim to address the needs of a fully connected society by enabling services and applications on a unified infrastructure.
- 5G transitions from centralized architectures to edge computing with multiple points-of-presence (PoPs)
- Low-latency, high-bandwidth applications benefit from edge computing, e.g. VR/AR.
- The MARSAL vision for 5G and B5G is focused on advancing capabilities of telecommunications networks. Its key enablers are (1) CN deployments that allow dynamic resource sharing, faster time-to-market and automation, and (2) end-to-end monitoring to manage the complex infrastructures (compute, storage, network, RAN).
- Monitoring in essential in Multi-Tenant Networks for maintaining KPIs across domains, enabling network operators and slice owners to validate SLAs and optimize operations.
- Existing research focuses on CN deployments or monitoring separately.
- This paper contribution is to present a unified experimental platform combining CN 5g core deployment and end-to-end monitoring.
  
### `II. Related Work`
- Studies focus either on cloud-native 5G deployments or end-to-end monitoring systems, but not both together.
- As for CN deployment studies, the studies often rely on partial implementation and lack comprehensive monitoring.
- As for system monitoring studies, they often exclude RAN metrics or lack containerized 5g core deployment.
- This paper proposes a framework that integrates both aspects, using containerized network functions (CNFs) orchestrated by Kubernetes. The paper also demonstrates the system through practical scenarios like UPF re-selection and user mobility.

### `III. Cloud-Native 5G Experimental Platform`
- ...

### `IV. End-to-End Monitoring: From Core to RAN`
- ...

### `V. Use Case Evaluation`
- ...

### `VI. Conclusions`
- ...

## Questions/Discussion Points

- Example to understand the concept of multi-tenant environments (e.g. those enabled by 5g network slicing):
    - Tenant A operates a streaming service and requires low-latency, high-bandwidth connectivity.
    - Tenant B runs IoT applications, requiring high reliability but lower bandwidth.
    - Monitoring tools measure KPIs like latency, jitter, and reliability for each tenant's slice and provide feedback to the network operator. If Tenant A's slice experiences congestion, monitoring systems can trigger an optimization process to allocate more resources or reroute traffic.

## Links/Resources

- ...
