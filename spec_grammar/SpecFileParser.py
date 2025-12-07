# Generated from docs/SpecFile.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,
        0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,5,2,39,8,2,10,2,12,
        2,42,9,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,5,4,51,8,4,10,4,12,4,54,9,4,
        1,5,3,5,57,8,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,3,7,74,8,7,1,7,5,7,77,8,7,10,7,12,7,80,9,7,1,8,3,8,83,
        8,8,1,8,1,8,1,8,1,8,1,8,3,8,90,8,8,1,8,1,8,1,8,1,8,1,8,3,8,97,8,
        8,1,8,1,8,1,8,1,8,1,8,3,8,104,8,8,1,8,1,8,1,8,1,8,3,8,110,8,8,1,
        9,1,9,1,9,1,9,1,9,1,9,5,9,118,8,9,10,9,12,9,121,9,9,1,9,0,0,10,0,
        2,4,6,8,10,12,14,16,18,0,0,131,0,25,1,0,0,0,2,34,1,0,0,0,4,36,1,
        0,0,0,6,43,1,0,0,0,8,48,1,0,0,0,10,56,1,0,0,0,12,63,1,0,0,0,14,69,
        1,0,0,0,16,109,1,0,0,0,18,111,1,0,0,0,20,24,3,2,1,0,21,24,5,19,0,
        0,22,24,5,20,0,0,23,20,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,27,
        1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,
        28,29,5,0,0,1,29,1,1,0,0,0,30,35,3,4,2,0,31,35,3,8,4,0,32,35,3,12,
        6,0,33,35,3,14,7,0,34,30,1,0,0,0,34,31,1,0,0,0,34,32,1,0,0,0,34,
        33,1,0,0,0,35,3,1,0,0,0,36,40,5,2,0,0,37,39,3,6,3,0,38,37,1,0,0,
        0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,5,1,0,0,0,42,40,1,
        0,0,0,43,44,5,16,0,0,44,45,5,1,0,0,45,46,5,17,0,0,46,47,5,18,0,0,
        47,7,1,0,0,0,48,52,5,3,0,0,49,51,3,10,5,0,50,49,1,0,0,0,51,54,1,
        0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,9,1,0,0,0,54,52,1,0,0,0,55,
        57,5,14,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,10,
        0,0,59,60,5,1,0,0,60,61,5,17,0,0,61,62,5,18,0,0,62,11,1,0,0,0,63,
        64,5,4,0,0,64,65,5,6,0,0,65,66,5,7,0,0,66,67,5,9,0,0,67,68,3,18,
        9,0,68,13,1,0,0,0,69,70,5,5,0,0,70,71,5,6,0,0,71,73,5,7,0,0,72,74,
        5,8,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,78,1,0,0,0,75,77,3,16,8,0,
        76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,15,1,
        0,0,0,80,78,1,0,0,0,81,83,5,14,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,
        84,1,0,0,0,84,85,5,10,0,0,85,86,5,1,0,0,86,87,5,17,0,0,87,110,5,
        18,0,0,88,90,5,14,0,0,89,88,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,
        91,92,5,11,0,0,92,93,5,1,0,0,93,94,5,17,0,0,94,110,5,18,0,0,95,97,
        5,14,0,0,96,95,1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,5,12,0,
        0,99,100,5,1,0,0,100,101,5,17,0,0,101,110,5,18,0,0,102,104,5,14,
        0,0,103,102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,5,13,
        0,0,106,107,5,1,0,0,107,108,5,17,0,0,108,110,5,18,0,0,109,82,1,0,
        0,0,109,89,1,0,0,0,109,96,1,0,0,0,109,103,1,0,0,0,110,17,1,0,0,0,
        111,112,5,15,0,0,112,113,5,17,0,0,113,119,5,18,0,0,114,115,5,15,
        0,0,115,116,5,17,0,0,116,118,5,18,0,0,117,114,1,0,0,0,118,121,1,
        0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,19,1,0,0,0,121,119,1,0,
        0,0,14,23,25,34,40,52,56,73,78,82,89,96,103,109,119
    ]

class SpecFileParser ( Parser ):

    grammarFileName = "SpecFile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'REQUIREMENT'", "'TEST_CASE'", "'INTEGRATION_TEST'", 
                     "'HUMAN_REVIEW'", "'*'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "METADATA_HEADER", "GLOBAL_HEADER", 
                      "EPIC_HEADER", "FEATURE_HEADER", "ID_FIELD", "DESCRIPTION_FIELD", 
                      "NOTES_FIELD", "FEATURES_HEADER", "REQUIREMENT", "TEST_CASE", 
                      "INTEGRATION_TEST", "HUMAN_REVIEW", "STAR", "DASH", 
                      "KEY", "VALUE", "NEWLINE", "BLANK_LINE", "COMMENT", 
                      "WS" ]

    RULE_specfile = 0
    RULE_section = 1
    RULE_metadata_section = 2
    RULE_metadata_entry = 3
    RULE_global_section = 4
    RULE_global_entry = 5
    RULE_epic_section = 6
    RULE_feature_section = 7
    RULE_feature_item = 8
    RULE_feature_list = 9

    ruleNames =  [ "specfile", "section", "metadata_section", "metadata_entry", 
                   "global_section", "global_entry", "epic_section", "feature_section", 
                   "feature_item", "feature_list" ]

    EOF = Token.EOF
    T__0=1
    METADATA_HEADER=2
    GLOBAL_HEADER=3
    EPIC_HEADER=4
    FEATURE_HEADER=5
    ID_FIELD=6
    DESCRIPTION_FIELD=7
    NOTES_FIELD=8
    FEATURES_HEADER=9
    REQUIREMENT=10
    TEST_CASE=11
    INTEGRATION_TEST=12
    HUMAN_REVIEW=13
    STAR=14
    DASH=15
    KEY=16
    VALUE=17
    NEWLINE=18
    BLANK_LINE=19
    COMMENT=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SpecfileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SpecFileParser.EOF, 0)

        def section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecFileParser.SectionContext)
            else:
                return self.getTypedRuleContext(SpecFileParser.SectionContext,i)


        def BLANK_LINE(self, i:int=None):
            if i is None:
                return self.getTokens(SpecFileParser.BLANK_LINE)
            else:
                return self.getToken(SpecFileParser.BLANK_LINE, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(SpecFileParser.COMMENT)
            else:
                return self.getToken(SpecFileParser.COMMENT, i)

        def getRuleIndex(self):
            return SpecFileParser.RULE_specfile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecfile" ):
                listener.enterSpecfile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecfile" ):
                listener.exitSpecfile(self)




    def specfile(self):

        localctx = SpecFileParser.SpecfileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_specfile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1572924) != 0):
                self.state = 23
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2, 3, 4, 5]:
                    self.state = 20
                    self.section()
                    pass
                elif token in [19]:
                    self.state = 21
                    self.match(SpecFileParser.BLANK_LINE)
                    pass
                elif token in [20]:
                    self.state = 22
                    self.match(SpecFileParser.COMMENT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(SpecFileParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metadata_section(self):
            return self.getTypedRuleContext(SpecFileParser.Metadata_sectionContext,0)


        def global_section(self):
            return self.getTypedRuleContext(SpecFileParser.Global_sectionContext,0)


        def epic_section(self):
            return self.getTypedRuleContext(SpecFileParser.Epic_sectionContext,0)


        def feature_section(self):
            return self.getTypedRuleContext(SpecFileParser.Feature_sectionContext,0)


        def getRuleIndex(self):
            return SpecFileParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)




    def section(self):

        localctx = SpecFileParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_section)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.metadata_section()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.global_section()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.epic_section()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.feature_section()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Metadata_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METADATA_HEADER(self):
            return self.getToken(SpecFileParser.METADATA_HEADER, 0)

        def metadata_entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecFileParser.Metadata_entryContext)
            else:
                return self.getTypedRuleContext(SpecFileParser.Metadata_entryContext,i)


        def getRuleIndex(self):
            return SpecFileParser.RULE_metadata_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadata_section" ):
                listener.enterMetadata_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadata_section" ):
                listener.exitMetadata_section(self)




    def metadata_section(self):

        localctx = SpecFileParser.Metadata_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_metadata_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(SpecFileParser.METADATA_HEADER)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 37
                self.metadata_entry()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Metadata_entryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(SpecFileParser.KEY, 0)

        def VALUE(self):
            return self.getToken(SpecFileParser.VALUE, 0)

        def NEWLINE(self):
            return self.getToken(SpecFileParser.NEWLINE, 0)

        def getRuleIndex(self):
            return SpecFileParser.RULE_metadata_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetadata_entry" ):
                listener.enterMetadata_entry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetadata_entry" ):
                listener.exitMetadata_entry(self)




    def metadata_entry(self):

        localctx = SpecFileParser.Metadata_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_metadata_entry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(SpecFileParser.KEY)
            self.state = 44
            self.match(SpecFileParser.T__0)
            self.state = 45
            self.match(SpecFileParser.VALUE)
            self.state = 46
            self.match(SpecFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GLOBAL_HEADER(self):
            return self.getToken(SpecFileParser.GLOBAL_HEADER, 0)

        def global_entry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecFileParser.Global_entryContext)
            else:
                return self.getTypedRuleContext(SpecFileParser.Global_entryContext,i)


        def getRuleIndex(self):
            return SpecFileParser.RULE_global_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_section" ):
                listener.enterGlobal_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_section" ):
                listener.exitGlobal_section(self)




    def global_section(self):

        localctx = SpecFileParser.Global_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_global_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(SpecFileParser.GLOBAL_HEADER)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==14:
                self.state = 49
                self.global_entry()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_entryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUIREMENT(self):
            return self.getToken(SpecFileParser.REQUIREMENT, 0)

        def VALUE(self):
            return self.getToken(SpecFileParser.VALUE, 0)

        def NEWLINE(self):
            return self.getToken(SpecFileParser.NEWLINE, 0)

        def STAR(self):
            return self.getToken(SpecFileParser.STAR, 0)

        def getRuleIndex(self):
            return SpecFileParser.RULE_global_entry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_entry" ):
                listener.enterGlobal_entry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_entry" ):
                listener.exitGlobal_entry(self)




    def global_entry(self):

        localctx = SpecFileParser.Global_entryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_global_entry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 55
                self.match(SpecFileParser.STAR)


            self.state = 58
            self.match(SpecFileParser.REQUIREMENT)
            self.state = 59
            self.match(SpecFileParser.T__0)
            self.state = 60
            self.match(SpecFileParser.VALUE)
            self.state = 61
            self.match(SpecFileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Epic_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EPIC_HEADER(self):
            return self.getToken(SpecFileParser.EPIC_HEADER, 0)

        def ID_FIELD(self):
            return self.getToken(SpecFileParser.ID_FIELD, 0)

        def DESCRIPTION_FIELD(self):
            return self.getToken(SpecFileParser.DESCRIPTION_FIELD, 0)

        def FEATURES_HEADER(self):
            return self.getToken(SpecFileParser.FEATURES_HEADER, 0)

        def feature_list(self):
            return self.getTypedRuleContext(SpecFileParser.Feature_listContext,0)


        def getRuleIndex(self):
            return SpecFileParser.RULE_epic_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEpic_section" ):
                listener.enterEpic_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEpic_section" ):
                listener.exitEpic_section(self)




    def epic_section(self):

        localctx = SpecFileParser.Epic_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_epic_section)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(SpecFileParser.EPIC_HEADER)
            self.state = 64
            self.match(SpecFileParser.ID_FIELD)
            self.state = 65
            self.match(SpecFileParser.DESCRIPTION_FIELD)
            self.state = 66
            self.match(SpecFileParser.FEATURES_HEADER)
            self.state = 67
            self.feature_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Feature_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FEATURE_HEADER(self):
            return self.getToken(SpecFileParser.FEATURE_HEADER, 0)

        def ID_FIELD(self):
            return self.getToken(SpecFileParser.ID_FIELD, 0)

        def DESCRIPTION_FIELD(self):
            return self.getToken(SpecFileParser.DESCRIPTION_FIELD, 0)

        def NOTES_FIELD(self):
            return self.getToken(SpecFileParser.NOTES_FIELD, 0)

        def feature_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecFileParser.Feature_itemContext)
            else:
                return self.getTypedRuleContext(SpecFileParser.Feature_itemContext,i)


        def getRuleIndex(self):
            return SpecFileParser.RULE_feature_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature_section" ):
                listener.enterFeature_section(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature_section" ):
                listener.exitFeature_section(self)




    def feature_section(self):

        localctx = SpecFileParser.Feature_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_feature_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SpecFileParser.FEATURE_HEADER)
            self.state = 70
            self.match(SpecFileParser.ID_FIELD)
            self.state = 71
            self.match(SpecFileParser.DESCRIPTION_FIELD)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 72
                self.match(SpecFileParser.NOTES_FIELD)


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                self.state = 75
                self.feature_item()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Feature_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUIREMENT(self):
            return self.getToken(SpecFileParser.REQUIREMENT, 0)

        def VALUE(self):
            return self.getToken(SpecFileParser.VALUE, 0)

        def NEWLINE(self):
            return self.getToken(SpecFileParser.NEWLINE, 0)

        def STAR(self):
            return self.getToken(SpecFileParser.STAR, 0)

        def TEST_CASE(self):
            return self.getToken(SpecFileParser.TEST_CASE, 0)

        def INTEGRATION_TEST(self):
            return self.getToken(SpecFileParser.INTEGRATION_TEST, 0)

        def HUMAN_REVIEW(self):
            return self.getToken(SpecFileParser.HUMAN_REVIEW, 0)

        def getRuleIndex(self):
            return SpecFileParser.RULE_feature_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature_item" ):
                listener.enterFeature_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature_item" ):
                listener.exitFeature_item(self)




    def feature_item(self):

        localctx = SpecFileParser.Feature_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_feature_item)
        self._la = 0 # Token type
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 81
                    self.match(SpecFileParser.STAR)


                self.state = 84
                self.match(SpecFileParser.REQUIREMENT)
                self.state = 85
                self.match(SpecFileParser.T__0)
                self.state = 86
                self.match(SpecFileParser.VALUE)
                self.state = 87
                self.match(SpecFileParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 88
                    self.match(SpecFileParser.STAR)


                self.state = 91
                self.match(SpecFileParser.TEST_CASE)
                self.state = 92
                self.match(SpecFileParser.T__0)
                self.state = 93
                self.match(SpecFileParser.VALUE)
                self.state = 94
                self.match(SpecFileParser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 95
                    self.match(SpecFileParser.STAR)


                self.state = 98
                self.match(SpecFileParser.INTEGRATION_TEST)
                self.state = 99
                self.match(SpecFileParser.T__0)
                self.state = 100
                self.match(SpecFileParser.VALUE)
                self.state = 101
                self.match(SpecFileParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==14:
                    self.state = 102
                    self.match(SpecFileParser.STAR)


                self.state = 105
                self.match(SpecFileParser.HUMAN_REVIEW)
                self.state = 106
                self.match(SpecFileParser.T__0)
                self.state = 107
                self.match(SpecFileParser.VALUE)
                self.state = 108
                self.match(SpecFileParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Feature_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(SpecFileParser.DASH)
            else:
                return self.getToken(SpecFileParser.DASH, i)

        def VALUE(self, i:int=None):
            if i is None:
                return self.getTokens(SpecFileParser.VALUE)
            else:
                return self.getToken(SpecFileParser.VALUE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(SpecFileParser.NEWLINE)
            else:
                return self.getToken(SpecFileParser.NEWLINE, i)

        def getRuleIndex(self):
            return SpecFileParser.RULE_feature_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFeature_list" ):
                listener.enterFeature_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFeature_list" ):
                listener.exitFeature_list(self)




    def feature_list(self):

        localctx = SpecFileParser.Feature_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_feature_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(SpecFileParser.DASH)
            self.state = 112
            self.match(SpecFileParser.VALUE)
            self.state = 113
            self.match(SpecFileParser.NEWLINE)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 114
                self.match(SpecFileParser.DASH)
                self.state = 115
                self.match(SpecFileParser.VALUE)
                self.state = 116
                self.match(SpecFileParser.NEWLINE)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





