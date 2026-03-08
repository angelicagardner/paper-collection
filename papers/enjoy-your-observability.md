---
title: "Enjoy your observability: an industrial survey of microservice tracing and analysis"
labels: "microservices, observability, tracing"
year: 2022
---

# Enjoy your observability: an industrial survey of microservice tracing and analysis

**Author(s):** Bowen Li, Xin Peng, Qilin Xiang, Hanzhang Wang, Tao Xie, Jun Sun, and Xuanzhe Liu

**Paper URL:** https://dl.acm.org/doi/10.1007/s10664-021-10063-9

**Pages:** 28

**Summary:** This paper is an industrial survey interviewing developers and operation engineers from 10 companies about how they have implemented microservice tracing and analysis. The results provides input to clarify whether the existing approaches fulfill required observability.

## Sections Summary

### `1. Introduction`

- Microservice systems may include hundreds to thousands services running in cloud infrastructure with service instances being created/destroyed dynamically. The run-time environments can exist of a mix of physical machines, virtual machines and containers.

- Distributed tracing is an important means to achieve observability in microservice architecture by tracing requests as they flow between services.

- The OpenTracing project provides a language-neutral data model for distributed tracing, defining basic concepts such as span and trace.

- A large microservice system may produce up to trillions of traces per second and each trace may involve a complex invocation chain spanning many services and even multiple data centers.

- The trace analysis following need to meet different purposes such as anomaly detection, fault analysis and debugging.
  
### `2. Background`

- ...

### `3. Methodology`
- ...

### `4. Results`
- ...

### `5. Discussion`
- ...

### `6. Related Work`
- ...

## Questions/Discussion Points

- ...

## Links/Resources

- ...