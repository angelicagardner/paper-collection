---
title: "Cloud-Native Observability: The Many-Faceted Benefits of Structured and Unified Logging—A Multi-Case Study"
labels: "cloud native, logging, observability"
year: 2022
---

# Cloud-Native Observability: The Many-Faceted Benefits of Structured and Unified Logging—A Multi-Case Study

**Author(s):** Nane Kratzke

**Paper URL:** https://www.researchgate.net/publication/363846034_Cloud-Native_Observability_The_Many-Faceted_Benefits_of_Structured_and_Unified_Logging-A_Multi-Case_Study

**Pages:** 23

**Summary:** This study proposes an integrated approach to observability by using a unified Python logging library and a structured logging architecture to merge metrics, logs and traces which has historically been three separate data streams. The researchers demonstrated that this unification is possible using existing toolchains and can efficiently process thousands of events per minute in real-world scenarios.

## Sections Summary

### `1. Introduction`

- The paper argues that observability in cloud-native systems can be achieved by logging structured events to stdout (which is simple).

- They define observability as the ability to infer a system’s internal state based on its external outputs.

- The authors argue that observability must be a core consideration during the initial design phase. It was traditionally an Operations (Ops) task but is migrating to Development (Dev). 
  
### `2. Problem Description`

- The fundamental problem: while we have better tools than ever, we’ve built data silos that make understanding complex systems harder than it needs to be.

- Because the three pillars (metrics, traces, logs) are treated as separate technologies, developers face a high instrumentation tax.

- The paper argues that logs, metrics, and traces are all just different forms of Time Series Analysis. The research question is: Can we simplify the process by using a unified instrumentation approach based on the simplest form (logs) and extend it to cover metrics and traces?

- The author argues that OTel is a unified protocol, while they are looking for a unified mental model. Instead of, like OpenTelemetry, have a Metrics API + Traces API + Logs API - their approach suggests to just log a structured event (a JSON object to stdout). The devs don't decide if it's a metric or a trace at the code level; it's the observability pipeline that later decide if that log should be counted as a metric or linked as a trace.

### `3. Methodology`

- The study utilizes "Action Research" which is a methodology specifically for collaboration between academia and industry. It focuses on solving a practical problem while simultaneously generating scientific knowledge.

- The research followed a four-step iterative cycle: Diagnosis, Prototyping, Evaluation, Learning Transfer.

- The researchers tested their unified logging theory across four distinct use cases:
	- UC1 (Qualitative) with basic events in an online code editor.
	- UC2 (Distributed Tracing) by tracking events across multiple services in the same code editor.
	- UC3 (Quantitative) by monitoring infrastructure data from a Kubernetes platform.
	- UC4 (High-Volume) by stress-testing the theory using a massive stream of Twitter data (the stock/crypto symbols).

### `4. Results of the Software-Prototyping`

- Now the authors turn theory into a tool. They lean on Factor XI (Logs) of the 12-Factor App methodology. This factor states that an app should never manage its own log files, it should stream events to stdout and let the execution environment handle the routing and storage.

- Unstructured logs require complex, slow text parsing (regex) to extract data while structured logs (in JSON) allows databases to index and search data instantly without expensive parsing.

- Everything follows one path: App → stdout → Log Forwarder → Analytical Database (e.g., Elasticsearch). The author developed a Python library where:
	- Every event gets a unique ID and timestamps.
	- It can link events within a single process to show hierarchy (parent-child relationships).
	- It pulls Trace IDs from incoming requests and attaches them to outgoing requests, allowing a trace to be reconstructed from separate log entries in different services.
	- Quantitative data (metrics) is included as a key-value pair in a log line.

### `5. Evaluation of the Logging Prototype`

- UC1 & UC2: The researchers successfully visualized the "logs-turned-traces" in a Kibana dashboard.

- UC3: This UC proved that infrastructure health can be tracked long-term using only the logging pipeline, i.e. structured logs can replace metrics.

- UC4: Phase 1 was a 10-day test to see what Twitter/X looks like normally. They found that only 1 in 100 tweets mentioned a stock symbol. Phase 2 was a 6-month study focusing on specific financial symbols where they captured the massive Terra Luna crash in May 2022.

- To summarize, the researchers are demonstrating that the source of the data doesn't matter, if it can be turned into a JSON object and pipe it to stdout, it can be observed.

### `6. Discussion`

- Lessons learned included:
	- Use log levels and don't just log errors.
	- Apps should never handle log routing but rely on the runtime environment to move data.
	- Push parent metadata into child events to achieve context injection. While this increases storage size, it makes searching and correlating data in the database much easier.
	- Don't calculate averages or medians in the code.

- Study Limitations (Threats to Validity) included:
	- The authors focused on logs and metrics while distributed tracing was only analyzed marginally.
	- The approach is not suitable for hard real-time systems with latency constraints.
	- The results are limited to Python 3 and the ELK stack.
	- The authors did not push the system until it broke so the absolute limit is unknown - tests reached 10,000 events per minute.

### `7. Related Work`

- Companies like Datadog, Dynatrace, and New Relic already offer unified observability. However, these are expensive managed services. The research prototype (log12) aims to solve the problem at the instrumentation level (in the code) using a lightweight, open approach.

- OTel and Service Meshes, like Istio, have a major advantage with auto-instrumentation. These tools can inject monitoring into an app without the developer writing any code which is a feature the log12 prototype lacks.

- The author notes that most academic papers are narrow focusing only on one thing like log parsing or security whereas this study looks from a holistic view of distributed systems.

## Questions/Discussion Pointsd

- The researchers intended to test the unified logging solution by tracking financial symbols ($USD, $AAPL) on Twitter/X and accidentally captured the 2022 "crypto winter." This was not part of their core thesis. 

- While stdout is simple it can become a bottleneck (since writing to stdout is a blocking operation in some languages/environments) or lead to massive storage costs if not filtered aggressively.

- OTel is good at context propagation, doing this through manual logging (where the dev must call .inject()) is more risk of broken traces (missing context) due to human error.

- Critique towards the Action Research methodology is that people doing the research are often the ones building the tool which can lead to confirmation bias because the researchers want their prototype to work so they might subconsciously interpret the data in a way that favors their theory.

- This wasn't a controlled experiment, i.e. one team would have used OpenTelemetry and another used log12 on the same task => difficult to prove one way is objectively better.

- The log12 approach could perhaps be a solution for systems that are too big for basic print statements but too small for the massive overhead of an enterprise OpenTelemetry setup.

## Links/Resources

- [The Prototype Logging Framework log12](https://github.com/nkratzke/log12)
