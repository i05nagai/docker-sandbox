from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


class CountWord(beam.DoFn):

    def process(self, element):
        print(element)
        return [len(" ".join(element[1]).split())]


def main():
    lorem = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Quisque a sapien eleifend, lacinia dui vitae, rhoncus dui.
Aenean tristique enim sit amet ligula malesuada, quis porta ante cursus.
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
    lorem = lorem.split('\n')
    #
    # An example of simple join (i.e. GroupByKey)
    #
    p = beam.Pipeline(options=pipeline_options.PipelineOptions())
    #
    # data
    #
    data = [
        ('amy', lorem[0]),
        ('carl', lorem[1]),
        ('julia', lorem[2]),
        ('carl', lorem[3]),
        ('carl', lorem[4]),
        ('carl', lorem[5]),
    ]
    path_output = os.path.join(PATH_TO_THIS_DIR, 'data.txt')
    p_data = p | 'create_data' >> beam.Create(data)
    p_data | 'write_data' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')
    #
    # wordcount
    #
    wordcount = (p_data
                 | beam.GroupByKey()
                 | beam.ParDo(CountWord()))
    path_output = os.path.join(PATH_TO_THIS_DIR, 'wordcount.txt')
    wordcount | 'write_wordcount' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')
    #
    # wait
    #
    result = p.run()
    result.wait_until_finish()


if __name__ == '__main__':
    main()
