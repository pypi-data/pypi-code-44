from ....datasources import Datasource
from ....datasources.meta import extractors, frequencies, mappers
from ....dependencies import DependentSet


class Revision(DependentSet):

    def __init__(self, name, regexes, wikitext_revision, exclusions, wrapping,
                 text_preprocess):
        super().__init__(name)
        if text_preprocess is not None:
            self.text = Datasource(
                name + ".preprocessed_text",
                depends_on=[wikitext_revision.text],
                process=text_preprocess)
        else:
            self.text = wikitext_revision.text

        self.matches = extractors.regex(
            regexes, self.text,
            name=name + ".matches",
            exclusions=exclusions,
            wrapping=wrapping
        )
        self.match_frequency = frequencies.table(
            mappers.lower_case(self.matches),
            name=name + ".match_frequency",
        )

        if hasattr(wikitext_revision, 'parent'):
            self.parent = Revision(name + ".parent", regexes,
                                   wikitext_revision.parent,
                                   exclusions=exclusions,
                                   wrapping=wrapping,
                                   text_preprocess=text_preprocess)

        if hasattr(wikitext_revision, 'diff'):
            self.diff = Diff(name + ".diff", regexes,
                             wikitext_revision.diff, self,
                             exclusions=exclusions,
                             wrapping=wrapping,
                             text_preprocess=text_preprocess)


class Diff(DependentSet):

    def __init__(self, name, regexes, wikitext_diff,
                 revision, exclusions, wrapping, text_preprocess):
        super().__init__(name)

        if text_preprocess is not None:
            segments_added = PreprocessedSegments(
                name + ".preprocessed_segments_added",
                wikitext_diff.segments_added,
                text_preprocess)
            segments_removed = Datasource(
                name + ".preprocessed_segments_removed",
                wikitext_diff.segments_removed,
                text_preprocess)
        else:
            segments_added = wikitext_diff.segments_added
            segments_removed = wikitext_diff.segments_removed

        self.matches_added = extractors.regex(
            regexes, segments_added,
            name=name + ".matches_added",
            exclusions=exclusions,
            wrapping=wrapping
        )
        self.matches_removed = extractors.regex(
            regexes, segments_removed,
            name=name + ".matches_removed",
            exclusions=exclusions,
            wrapping=wrapping
        )

        self.match_delta = frequencies.delta(
            revision.parent.match_frequency,
            revision.match_frequency,
            name=name + ".match_delta"
        )
        self.match_prop_delta = frequencies.prop_delta(
            revision.parent.match_frequency,
            self.match_delta,
            name=name + ".match_prop_delta"
        )


class PreprocessedSegments(Datasource):

    def __init__(self, name, segments, text_preprocess):
        self.text_preprocess = text_preprocess

    def process(self, segments):
        return [self.text_preprocess(segment) for segment in segments]
