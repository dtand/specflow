[FEATURE: Valid moves]
ID: REQ-MOV-001
DESCRIPTION: "Allow moving cards between tableau piles following Solitaire rules"
DEPENDS_ON: REQ-TAB-001

*TEST_CASE: "Move valid card between piles" {id="TC-MOV-001"}
*TEST_CASE: "Reject invalid moves" {id="TC-MOV-002"}
*INTEGRATION_TEST: "Play through a sequence of valid moves" {id="IT-MOV-001"}
*HUMAN_REVIEW: "Confirm move logic matches Solitaire rules" 
