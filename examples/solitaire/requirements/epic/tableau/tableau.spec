[FEATURE: Tableau setup]
ID: REQ-TAB-001
DESCRIPTION: "Deal cards into seven piles with increasing counts, last card face up"
DEPENDS_ON: REQ-DEC-001
NOTES: "Use lists to represent piles"

*TEST_CASE: "Tableau has 7 piles with correct card counts" {id="TC-TAB-001"}
*TEST_CASE: "Only last card in each pile is face up" {id="TC-TAB-002"}
*INTEGRATION_TEST: "Initialize tableau from shuffled deck" {id="IT-TAB-001"}
*HUMAN_REVIEW: "Verify tableau setup matches Solitaire rules"
