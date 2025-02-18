## Submission

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


### Output (Simulated Fake Data Scenario):

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