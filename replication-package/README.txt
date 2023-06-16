There are 4 folders in this replication package. 

1. Code - This folder contains the source files to calculate agreements

To calculate the agreement amongst the coders for privacy requirements extraction and classification steps (Section 3-A-1) and 3-A-2)), use these files:
- Source file: Requirement extraction - Fleiss calculation
- Data:	Coding results - requirements extraction - GDPR.csv
	Coding results - requirements extraction - ISO.csv
	Coding results - requirements classification.csv

To calculate the agreement between coders for issue reports classification step (Section 4-B), use these files:
- Source file: Issue reports classification - reliability assessment calculation
- Data: Chrome-A1A2-task.csv 
	Chrome-A1A3-task.csv 
	Moodle-A1A2-task.csv
	Moodle-A1A3-task.csv

To run the statistical tests between privacy and non-privacy issues (Section 4-D RQ2), use these files:
- Source file: Privacy vs non-privacy.py
- Data:	Chrome-sample-privacy.csv
	Chrome-sample-nonprivacy.csv
	Moodle-sample-privacy.csv
	Moodle-sample-nonprivacy.csv

2. Data - This folder contains the data files used in the study

Privacy requirements development (Section 3)
- Coding results - requirements extraction - GDPR.xlxs: contains a list of numbered GDPR clauses shortlisted to determine if those clauses can be extracted as privacy requirements (0 is 'NO' and 1 is 'YES')
- Coding results - requirements extraction - ISO.xlxs: contains a list of numbered ISO/IEC 29100 statements shortlisted to determine if those clauses can be extracted as privacy requirements (0 is 'NO' and 1 is 'YES')
- Coding results - requirements classification.csv: contains the values that determine categories for each statement (Value 0 means the lawfulness, fairness and transparency goal - Value 6 means accountability goal)

Issue reports classification (Section 4)
Raw data
- Chrome - A1.csv: contains coder1's issue IDs and requirements matrix of Chrome dataset
- Chrome - A2.csv: contains coder2's issue IDs and requirements matrix of Chrome dataset
- Chrome - A3.csv: contains coder3's issue IDs and requirements matrix of Chrome dataset
- Moodle - A1.csv: contains coder1's issue IDs and requirements matrix of Moodle dataset
- Moodle - A2.csv: contains coder2's issue IDs and requirements matrix of Moodle dataset
- Moodle - A3.csv: contains coder3's issue IDs and requirements matrix of Moodle dataset
- Chrome-sample-privacy.csv: contains issue ID, summary and description, resolution time, number of comments, issue types, number of contributors and priorityof privacy-related issues in Chrome
- Chrome-sample-nonprivacy.csv: contains issue ID, summary and description, resolution time, number of comments, issue types, number of contributors and priority of non-privacy issues in Chrome
- Moodle-sample-privacy.csv: contains issue ID, summary and description, resolution time, number of comments, issue types, number of contributors and priority of privacy-related issues in Moodle
- Moodle-sample-nonprivacy.csv: contains issue ID, summary and description, resolution time, number of comments, issue types, number of contributors and priority of non-privacy issues in Moodle

For reliability assessments (Section 4-C)
- Chrome-A1A2-task.csv: contains coder1's and coder2's issue IDs and requirements matrix of Chrome dataset
- Chrome-A1A3-task.csv: contains coder1's and coder3's issue IDs and requirements matrix of Chrome dataset
- Moodle-A1A2-task.csv: contains coder1's and coder2's issue IDs and requirements matrix of Moodle dataset
- Moodle-A1A3-task.csv: contains coder1's and coder3's issue IDs and requirements matrix of Moodle dataset

For occurrence calculation (Section 4-D)
- Chrome - Issues with labels: contains 896 issue reports with requirements matrix after disagreement resolution
- Moodle - Issues with labels: contains 478 issue reports with requirements matrix after disagreement resolution

Occurrence results
- Chrome - occurrences by requirements.csv: contains the percentage of requirement occurrences in Chrome issue reports
- Moodle - occurrences by requirements.csv: contains the percentage of requirement occurrences in Moodle issue reports
- Chrome - occurrences by categories.csv: contains the percentage of requirement occurrences by categories in Chrome issue reports
- Moodle - occurrences by categories.csv: contains the percentage of requirement occurrences by categories in Moodle issue reports
- number-of-issues-by-type.csv: contains the number of issue reports categorised by issue type in Chrome and Moodle projects.

3. Privacy-requirements-materials - This folder contains four files (see Section 3 in the paper):

- Mapping-across-regulations: this file shows an informal mapping between the GDPR principles, ISO/IEC 29100 principles, Thailand PDPA parts and APEC framework principles.
- Privacy-requirements-references: this file contains a full list of the privacy requirements with their references to the GDPR articles, ISO/IEC29100 principles, Thailand PDPA sections and APEC framework points.
- Privacy-requirements-taxonomy: this file contains a full version of privacy requirements taxonomy.
- Privacy-requirements-abstraction: this file contains some sample requirements derived from GDPR, ISO/IEC29100, Thailand PDPA and APEC privacy framework demonstrating that they are at the same level of abstraction.

4. Training-materials - This folder contains the materials used in the training sessions and the original of copy of GDPR. We cannot share ISO/IEC 29100 privacy framework document here since it violates the copyright license.