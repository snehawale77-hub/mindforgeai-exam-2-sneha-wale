# Q1: Workspace Architecture & Submission Workflow

## 1. Objective
To establish a high-availability, version-controlled workspace for Module Assessment 2 that ensures full traceability from local development through to final portal submission.

---

## 2. Technical Workflow Map


[Image of software development lifecycle workflow diagram]


---

## 3. Toolchain & Responsibility Matrix

### Phase 1: Workspace Initialization (VS Code)
* **Responsibility:** Project scaffolding and local environment management.
* **Technical Role:** Serves as the central IDE. Responsible for initializing the directory structure, managing local Git operations, and maintaining Markdown-based documentation for all sections.

### Phase 2: Execution & Data Pipeline (Jupyter/Colab)
* **Responsibility:** Logic implementation and data transformation.
* **Technical Role:** Serves as the computational engine. Responsible for executing the Python data analytics pipeline, validating data signals, and generating visual performance insights. Jupyter ensures a clear link between code, input, and output.

### Phase 3: Version Control (GitHub)
* **Responsibility:** Source code integrity and collaborative readiness.
* **Technical Role:** Serves as the canonical source of truth for the project. Responsible for versioning the `notebooks/`, `data/`, and `README.md` components. GitHub acts as the backup and the primary channel for the evaluators to inspect the codebase.

### Phase 4: Offline Digitization (Scanner)
* **Responsibility:** Theory documentation and algorithmic trace capture.
* **Technical Role:** Serves as the digitization bridge. Responsible for converting physical, handwritten algorithmic diagrams and memory traces (Section A & B) into a unified, high-fidelity PDF document.

### Phase 5: Secure Hosting (Google Drive)
* **Responsibility:** Asset storage and link-based access management.
* **Technical Role:** Serves as the secure storage bucket for non-code artifacts. Responsible for hosting the Scanned PDF and optional demo materials, with access strictly set to 'Viewer' to ensure persistence and integrity during the evaluation window.

### Phase 6: Final Aggregation (Student Portal)
* **Responsibility:** Submission fulfillment.
* **Technical Role:** Serves as the submission API. Responsible for aggregating the decentralized links (GitHub, Colab, Drive) into a single payload, accompanied by a structured technical summary for the reviewer.

---

## 4. Logical Workflow Summary
The workflow follows a **modular, decentralized architecture**: 
- **Coding** is localized for speed. 
- **Version Control** is cloud-based for reliability. 
- **Theory** is digitized for portability. 
- **Aggregation** is portal-based for finality.

By segmenting the responsibilities of each tool, we minimize the "Single Point of Failure" risk: if a specific cloud link fails, the evaluator can still access the complete repository via GitHub.