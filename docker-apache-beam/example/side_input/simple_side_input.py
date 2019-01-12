from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
import example.data as data


def write_to_file(pipeline, id_str):
    PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))
    path_output = os.path.join(PATH_TO_THIS_DIR, '{0}.txt'.format(id_str))
    (pipeline
     | 'write_{0}'.format(id_str) >> beam.io.WriteToText(path_output, file_name_suffix='.csv'))


def main():
    lorem = data.lorem_words
    with beam.Pipeline(options=pipeline_options.PipelineOptions()) as p:
        words = p | 'create_lorem' >> beam.Create(lorem)
        write_to_file(words, 'words')

        def filter_using_length(word, lower_bound, upper_bound=float('inf')):
            if lower_bound <= len(word) <= upper_bound:
                yield word

        # Construct a deferred side input.
        avg_word_len = (words
                        | beam.Map(len)
                        | beam.CombineGlobally(beam.combiners.MeanCombineFn()))
        write_to_file(avg_word_len, 'avg_word_len')

        # Call with explicit side inputs.
        small_words = words | 'small_words' >> beam.FlatMap(filter_using_length, 0, 3)
        write_to_file(small_words, 'small_words')

        # A single deferred side input.
        larger_than_average = (words | 'large' >> beam.FlatMap(
            filter_using_length,
            lower_bound=beam.pvalue.AsSingleton(avg_word_len)))
        write_to_file(larger_than_average, 'larger_than_average')

        # Mix and match.
        small_but_nontrivial = words | beam.FlatMap(
            filter_using_length,
            lower_bound=2,
            upper_bound=beam.pvalue.AsSingleton(avg_word_len))
        write_to_file(small_but_nontrivial, 'small_but_nontrivial')

        # We can also pass side inputs to a ParDo transform, which will get passed to its process method.
        # The first two arguments for the process method would be self and element.
        class FilterUsingLength(beam.DoFn):

            def process(self, element, lower_bound, upper_bound=float('inf')):
                if lower_bound <= len(element) <= upper_bound:
                    yield element

        # small word
        small_words_do_fn = words | 'small_words_do_fn' >> beam.ParDo(FilterUsingLength(), 0, 3)
        write_to_file(small_words_do_fn, 'small_words_do_fn')


if __name__ == '__main__':
    main()
