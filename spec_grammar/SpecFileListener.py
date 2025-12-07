# Generated from docs/SpecFile.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SpecFileParser import SpecFileParser
else:
    from SpecFileParser import SpecFileParser

# This class defines a complete listener for a parse tree produced by SpecFileParser.
class SpecFileListener(ParseTreeListener):

    # Enter a parse tree produced by SpecFileParser#specfile.
    def enterSpecfile(self, ctx:SpecFileParser.SpecfileContext):
        pass

    # Exit a parse tree produced by SpecFileParser#specfile.
    def exitSpecfile(self, ctx:SpecFileParser.SpecfileContext):
        pass


    # Enter a parse tree produced by SpecFileParser#section.
    def enterSection(self, ctx:SpecFileParser.SectionContext):
        pass

    # Exit a parse tree produced by SpecFileParser#section.
    def exitSection(self, ctx:SpecFileParser.SectionContext):
        pass


    # Enter a parse tree produced by SpecFileParser#metadata_section.
    def enterMetadata_section(self, ctx:SpecFileParser.Metadata_sectionContext):
        pass

    # Exit a parse tree produced by SpecFileParser#metadata_section.
    def exitMetadata_section(self, ctx:SpecFileParser.Metadata_sectionContext):
        pass


    # Enter a parse tree produced by SpecFileParser#metadata_entry.
    def enterMetadata_entry(self, ctx:SpecFileParser.Metadata_entryContext):
        pass

    # Exit a parse tree produced by SpecFileParser#metadata_entry.
    def exitMetadata_entry(self, ctx:SpecFileParser.Metadata_entryContext):
        pass


    # Enter a parse tree produced by SpecFileParser#global_section.
    def enterGlobal_section(self, ctx:SpecFileParser.Global_sectionContext):
        pass

    # Exit a parse tree produced by SpecFileParser#global_section.
    def exitGlobal_section(self, ctx:SpecFileParser.Global_sectionContext):
        pass


    # Enter a parse tree produced by SpecFileParser#global_entry.
    def enterGlobal_entry(self, ctx:SpecFileParser.Global_entryContext):
        pass

    # Exit a parse tree produced by SpecFileParser#global_entry.
    def exitGlobal_entry(self, ctx:SpecFileParser.Global_entryContext):
        pass


    # Enter a parse tree produced by SpecFileParser#epic_section.
    def enterEpic_section(self, ctx:SpecFileParser.Epic_sectionContext):
        pass

    # Exit a parse tree produced by SpecFileParser#epic_section.
    def exitEpic_section(self, ctx:SpecFileParser.Epic_sectionContext):
        pass


    # Enter a parse tree produced by SpecFileParser#feature_section.
    def enterFeature_section(self, ctx:SpecFileParser.Feature_sectionContext):
        pass

    # Exit a parse tree produced by SpecFileParser#feature_section.
    def exitFeature_section(self, ctx:SpecFileParser.Feature_sectionContext):
        pass


    # Enter a parse tree produced by SpecFileParser#feature_item.
    def enterFeature_item(self, ctx:SpecFileParser.Feature_itemContext):
        pass

    # Exit a parse tree produced by SpecFileParser#feature_item.
    def exitFeature_item(self, ctx:SpecFileParser.Feature_itemContext):
        pass


    # Enter a parse tree produced by SpecFileParser#feature_list.
    def enterFeature_list(self, ctx:SpecFileParser.Feature_listContext):
        pass

    # Exit a parse tree produced by SpecFileParser#feature_list.
    def exitFeature_list(self, ctx:SpecFileParser.Feature_listContext):
        pass



del SpecFileParser