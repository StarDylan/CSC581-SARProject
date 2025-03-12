# Submission

## Revision

### Insights

- Current implementation was a bit simple. We need to integrate an LLM to actually extract clues.

- There were also some feedback related to the documentation, which has been updated.

- Lastly, there was a suggestion for grouping clues for different cases (this is important for future development, but not necessary for this proof of concept).

### Modificatitons

- Implemented an LLM clue extractor which can be used to extract clues from forms or interviews.
- Updated the documentation to include the new feature.


#### Clue Extracting and Flagging

The base clue is: "A person was lost while hiking. He was last seen at the base of a mountain. He hates high elevation"

The LLM extracts the following clues:
`['The lost person was last seen at the base of a mountain.', 'The lost person hates high elevation.']`

The LLM then flagged these 2 clues as they are related and should be investigated.

This uses the Clue DB in the previous implementation.

### Selected Task: Clue Meister

ClueMeister              [[2025-01-30 ClueMeister Agent]]	

Clue prioritization, pattern recognition, inquiry initiation

Analyze and prioritize clues for investigation

Sort clues by criteria, identify patterns in clue sets, initiate further inquiries

Number of prioritized clues leading to actionable insights; Accuracy of pattern recognition in clue sets

Intelligence/Investigations Section, Field reports from search teams or drones capturing environmental clues

Operations Section Chief, MissingPersonProfiler	Subjectivity in interpretation, data quality

MissingPersonProfiler, PathExplorer	Natural language processing, clue management tools

Crucial for directing search efforts efficiently



### Basic Clue DB Usage (Simulated Fake Data Scenario):

Set Status to Active
```
{'status': 'updated', 'new_status': 'active'}
```

List Clues
```
{'clue_text': 
    'Clues:
      Clue ID #1: Test clue 1
      Clue ID #2: Test clue 2
      Clue ID #3: Missing person last seen at the park
      Clue ID #4: Missing Person has a tattoo on their left arm
      Clue ID #5: Missing Person loves to hide under slides in the park
    '}
```

Flag Clue 3
```
{'clue_id': 3}
```


Flag Clue 5
```
{'clue_id': 5}
```

Add query "Search the park for the missing person, check under the slides (see clues 3 + 5)"
```
{'response': 'Added Query'}
```

List clues again (show flagged output)
```
{'clue_text': 'Clues:
    Clue ID #1: Test clue 1

    Clue ID #2: Test clue 2

    Clue ID #3: Missing person last seen at the park (Already Flagged)

    Clue ID #4: Missing Person has a tattoo on their left arm

    Clue ID #5: Missing Person loves to hide under slides in the park (Already Flagged)
'}
```

## Setup


## Prerequisites

- Python 3.8 or higher
- pyenv (recommended for Python version management)
- pip (for dependency management)

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sar-project
```

2. Set up Python environment:
```bash
# Using pyenv (optional)
pyenv install 3.9.6  # or your preferred version
pyenv local 3.9.6

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```

4. Configure environment variables:

#### Google Gemini:
- add `GOOGLE_API_KEY` and `OPENAI_API_KEY` to `.env` file

Make sure to keep your `.env` file private and never commit it to version control.