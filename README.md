# TriAgent: Agentic AI for Healthcare Triage

An open-source agentic AI system that assists healthcare workers in triage, diagnosis and decision support - designed for deployment in low-resource or disconnected environments.

## Tech Stack

- Framework: CrewAI for agent orchestration and task flow
- Models: Open-source LLMs from Hugging Face Transformers
- Tools:
    - Retrieval-Augmented Generation (RAG) for medical knowledge retrieval
    - AutoML for immediate Biomarker identification
    - Core matrix/tensor ops

## Core Workflow

```plaintext
[Agent converses with user] 
-> [Identify significant features in medical databases/biobanks] 
-> [Perform AutoML to identify most significant biomarkers] 
-> [Research journals for evidence] 
-> [Split biomarkers into established and novel]
```

![Diagram](dev/diagram.png)

## Objectives

- Enable a modular, research-oriented AI triage assistant to support emergency departments.
- Enable intelligent query and search capability with advanced retrieval and reasoning pipelines.
- Reduce the risk of misdiagnosis with evidence-based insights.
- Make performance of open-source models similar to proprietary LLMs in this task.
- Maintain safe and appropriate data and privacy practices.

## Installation

Install the [uv](https://docs.astral.sh/uv/#highlights) package manager. Then:

```bash
uv sync
```


For development,
```bash
uv sync --all-extras
```

## Current Status

- Need to build a generative model to create synthetic data
- Generative model needs to include all sorts of biomarkers without discrimination
- To reduce latency we may require it to filter the ICD codes being considered
- This will be used for the rest of the agentic framework to use instead of existing health records