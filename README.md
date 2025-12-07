# specflow

The **Spec CLI** is the command‑line toolkit for the [Specflow](../) framework.  
It provides utilities to parse `.spec` files, generate requirement structures from EPIC manifests, track progress, and validate compliance with global rules.

---

## 🚀 Features

- **Initialize projects** from an EPIC spec file:
  - Creates epic folders, requirement subfolders, empty `.spec` templates, and `progress.yaml` trackers.
- **Parse specs** into JSON/AST for downstream tools.
- **Validate specs** against global requirements (language, naming conventions, docstrings, test coverage).
- **Track progress** by updating lifecycle states and test results in `progress.yaml`.
- **Resolve dependencies** and visualize requirement execution order.
- **Unified CLI** entry point for all operations.

---

## 📂 Project Layout


---

## 🛠️ Installation

Clone the repo and set up your environment:

```bash
git clone https://github.com/yourname/specflow.git
cd specflow
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --editable .
```

## Usage CLI
spec init requirements/epic-logging/epic.spec
spec validate requirements/epic-logging/epic.spec
spec update requirements/epic-logging/logging/progress.yaml --status TESTING --test TC-EL-001=PASS
spec graph requirements/epic-logging/epic.spec

## Example Workflow
1. Write an EPIC spec:
```
[METADATA]
PROJECT_NAME: Solitaire
REVISION: 1.0
AUTHOR: Daniel

[GLOBAL]
REQUIREMENT: Python 3.11+
REQUIREMENT: pytest for unit testing
REQUIREMENT: snake_case variable naming
REQUIREMENT: python virtual environment

[EPIC: Basic Solitaire Game]
ID: EPIC-001
DESCRIPTION: Implement a playable version of Solitaire with core rules and interactions
FEATURES: 
    - deck
    - tableau
    - moves
    - win_condition

```
2. Run spec init epic.spec → generates folders + empty requirement specs.

3. Fill in requirement specs with descriptions, tests, and human review checkpoints.

4. Use spec update to track progress as features are implemented and tested.



