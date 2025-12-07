[FEATURE: Win condition]
ID: REQ-WIN-001
DESCRIPTION: "Detect when all cards are moved to foundation piles in order"
DEPENDS_ON: REQ-MOV-001
NOTES: "Track foundation piles by suit"

*TEST_CASE: "Foundation piles accept cards in ascending order" {id="TC-WIN-001"}
*INTEGRATION_TEST: "Detect win when all cards are in foundations" {id="IT-WIN-001"}
*HUMAN_REVIEW: "Verify win detection matches Solitaire rules"
