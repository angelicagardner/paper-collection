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

- Service invocation chains enable understanding runtime service dependencies and the execution process of the requests, which makes them important for modern distributed systems.

- Trace = represents the total time a request takes as it moves through the entire system. It is identified by a unique Trace ID.

- Span = represents a specific operation within that journey. Every span has a start time, a duration, and a Span ID.

- Logs, traces and metrics are the pillars of observability. Logs include application logs, system logs, and span logs. Traces are produced by the distributed tracing system and restored from span logs. Metrics include both application metrics and system metrics.

### `3. Methodology`

- Study duration was 4 months.

- Qualitative research approach using interviews; 25 interviewees from 10 companies.

- Companies cover 5 different domains: e-commerice, entertainment, finance, manufacture and ERP.

- The procedure was divided into 3 parts: interview planning, interview process, and interview result analysis.

- It was required that the interviewees were knowledgeable about distributed tracing practices and engineering.

- Over 700 minutes of interview recordings were converted into text documents using speech recognition. Their own notes were combined with the text documents to complete the interview transcripts.

- Some follow-up interviews were conducted to learn missing details.

### `4. Results`

- Distributed tracing is less important for small microservice systems where number of services is small and invocation chains are short.

- Their tracing and analysis pipeline implementations follow similar structures: logging, collection, preprocessing, storage and analysis.

- Several pipeline implementations used a message bus to increase the reliability of log transmission and collection.

- Several pipeline implementations used a stream computing engine to achieve real-time processing of trace data.

- Large companies had a tendency to develop and maintain their own distributed tracing system instead of relying on open source solutions, due to strict requirements for reliability and performance of trace data processing as well as demand on customized trace analysis applications.

- More advanced solutions such as tracing-framework-based logging and agent-based log collection relieve developers from the implementation of distributed tracing.

- The companies widely follow the log content and format defined by the OpenTracing specification.

- Preprocessing usually included data formatting, metric aggregation and tail-based sampling.

- The huge amount of trace data has been the main challenge for trace analysis.

- Service mesh is emerging as an alternative solution for microservice tracing. In this solution, developers don't need to care about the implementation of microservice tracing. None of the companies included in this survey used service mesh.

### `5. Discussion`

- This survey indicates that microservice tracing and analysis is a new big data problem for software engineering.

- New challenges and opportunities presented include adaptive log sampling, data fusion for trace analysis, more intelligent trace analysis and business intelligence by trace analysis.

### `6. Related Work`
- ...

## Questions/Discussion Points

- In the results section (4) the authors mention the main challenge as the huge amount of trace data - but in the conclusion they mention the quality of data, the lack of trace data annotation and the ever-changing nature of microservice architecture as the main difficulties.
