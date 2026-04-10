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

- The fundamental problem: while we have better tools than ever, we’ve built "data silos" that make understanding complex systems harder than it needs to be.

- Because the three pillars (metrics, traces, logs) are treated as separate technologies, developers face a high "instrumentation tax."

- The paper argues that logs, metrics, and traces are all just different forms of Time Series Analysis. The research question is: Can we simplify the process by using a unified instrumentation approach based on the simplest form (logs) and extend it to cover metrics and traces?

- The author argues that OTel is a "unified protocol," while they are looking for a "unified mental model." Instead of, like OpenTelemetry, have a Metrics API + Traces API + Logs API - their approach suggests to just log a structured event (a JSON object to stdout). The devs don't decide if it's a metric or a trace at the code level; it's the observability pipeline that later decide if that log should be counted as a metric or linked as a trace.

### `3. Methodology`

- ...

### `4. Results of the Software-Prototyping`

- ...

### `5. Evaluation of the Logging Prototype`

- ...

### `6. Discussion`

- ...

### `7. Related Work`

- ...

## Questions/Discussion Pointsd

- The researchers intended to test the unified logging solution by tracking financial symbols ($USD, $AAPL) on Twitter/X and accidentally captured the 2022 "crypto winter." This was not part of their core thesis. 

- While stdout is simple it can become a bottleneck (since writing to stdout is a "blocking" operation in some languages/environments) or lead to massive storage costs if not filtered aggressively.

- OTel is good at context propagation but doing this through manual logging is very difficult so it would lead to missing context?

## Links/Resources

- ...
