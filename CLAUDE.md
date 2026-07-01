# CLAUDE.MD: THE INFRASTRUCTURE LAYER

## 1. MISSION & COMMAND INTENT
* **Mission:** To build the "AI Referee"—the infrastructure layer that governs, measures, and optimizes agentic output.
* **Vision:** To provide a system that is 5x cheaper and 7x faster than legacy manual environments.
* **Target Performance:** Outperform industry giants (Amazon, Google, Nvidia) by focusing on **Code Health** over raw output, eliminating technical debt at the source.

## 2. THE SYSTEM ARCHITECTURE (3rd-Grader Simple)
1.  **The Brain (Model):** Multi-model routing (Claude, Gemini, Grok) to avoid single-point failure.
2.  **The Memory (Data Layer):** A centralized "Notebook" hub for immutable brand voice and historical context.
3.  **The Workers (Agents):** Task-specific agents operating within Role-Based SOP templates.
4.  **The Referee (Governance):** An automated evaluation layer that scores every task for **Efficiency, Ease of Use, and Error-Density.**

## 3. CORE OPERATING PRINCIPLES (The Vorem Rules)
* **Systemize Before Scaling:** No feature is deployed without a supporting SOP.
* **Human-in-the-Loop:** AI does the labor; humans provide the Leadership, Ethos, and Pathos.
* **Zero Technical Debt:** Every line of code must be validated by the "AI Referee" against security and accessibility (WCAG) benchmarks.
* **Simple is Powerful:** All system communications must be understandable by a 3rd-grader.

## 4. DEVELOPMENT WORKFLOW (SOP Integration)
1.  **Baseline Loading:** Define "Command Intent" and Brand Voice before execution.
2.  **Quantitative Experimentation:** Measure performance in seconds, error counts, and lines of code.
3.  **The AI Referee Check:** Automated audit for "Quality Debt" and security vulnerabilities (targeting the 23.7% AI-vulnerability gap).
4.  **Keyword & Visual Seal:** Align technical output with the strategic mission.
5.  **Ethical Deployment:** Ensure compliance with "Responsible AI" standards and unbiased task assignment.

## 5. PROJECT STRUCTURE

```
src/referee/          ← Core engine (models, analyzers, orchestrator)
api/                  ← FastAPI REST server
cli/                  ← Click command-line interface
tests/                ← Pytest suite + fixtures
```

## 6. KEY COMMANDS

```bash
# Install
pip install -e ".[dev]"

# Run CLI audit
referee audit path/to/file.py

# Run REST API
uvicorn api.server:app --reload

# Run tests
pytest
```
