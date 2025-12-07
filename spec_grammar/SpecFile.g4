grammar SpecFile;

// Top-level rule
specfile
    : (section | BLANK_LINE | COMMENT)* EOF
    ;

section
    : metadata_section
    | global_section
    | epic_section
    | feature_section
    ;

metadata_section
    : METADATA_HEADER metadata_entry*
    ;

metadata_entry
    : KEY ':' VALUE NEWLINE
    ;

global_section
    : GLOBAL_HEADER global_entry*
    ;

global_entry
    : STAR? REQUIREMENT ':' VALUE NEWLINE
    ;

epic_section
    : EPIC_HEADER
      ID_FIELD
      DESCRIPTION_FIELD
      FEATURES_HEADER feature_list
    ;

feature_section
    : FEATURE_HEADER
      ID_FIELD
      DESCRIPTION_FIELD
      NOTES_FIELD?
      feature_item*
    ;

feature_item
    : STAR? REQUIREMENT ':' VALUE NEWLINE
    | STAR? TEST_CASE ':' VALUE NEWLINE
    | STAR? INTEGRATION_TEST ':' VALUE NEWLINE
    | STAR? HUMAN_REVIEW ':' VALUE NEWLINE
    ;

feature_list
    : DASH VALUE NEWLINE (DASH VALUE NEWLINE)*
    ;

METADATA_HEADER: '[METADATA]' NEWLINE;
GLOBAL_HEADER: '[GLOBAL]' NEWLINE;
EPIC_HEADER: '[EPIC:' WS? VALUE ']' NEWLINE;
FEATURE_HEADER: '[FEATURE:' WS? VALUE ']' NEWLINE;
ID_FIELD: 'ID:' VALUE NEWLINE;
DESCRIPTION_FIELD: 'DESCRIPTION:' VALUE NEWLINE;
NOTES_FIELD: 'NOTES:' VALUE NEWLINE;
FEATURES_HEADER: 'FEATURES:' NEWLINE;

REQUIREMENT: 'REQUIREMENT';
TEST_CASE: 'TEST_CASE';
INTEGRATION_TEST: 'INTEGRATION_TEST';
HUMAN_REVIEW: 'HUMAN_REVIEW';

STAR: '*';
DASH: '-';

KEY: [A-Z_]+;
VALUE: ~[\r\n]+;
NEWLINE: ('\r'? '\n');
BLANK_LINE: NEWLINE;
COMMENT: '#' ~[\r\n]* NEWLINE -> skip;
WS: [ \t]+ -> skip;