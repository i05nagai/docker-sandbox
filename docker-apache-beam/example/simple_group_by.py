from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def main():
    #
    # An example of simple join (i.e. GroupByKey)
    #
    p = beam.Pipeline(options=pipeline_options.PipelineOptions())
    #
    # email
    #
    emails_list = [
        ('amy', ('amy@example.com', '1')),
        ('carl', ('carl@example.com', '2')),
        ('julia', ('julia@example.com', '3')),
        ('carl', ('carl@email.com', '4')),
        ('carl', ('carl2@email.com', '2')),
        ('carl', ('carl3@email.com', '1')),
    ]
    path_output = os.path.join(PATH_TO_THIS_DIR, 'emails.txt')
    emails = p | 'create_emails' >> beam.Create(emails_list)
    emails | 'write_emails' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')
    #
    # gropu by
    #
    group_by = (emails
                | beam.GroupByKey())
    path_output = os.path.join(PATH_TO_THIS_DIR, 'gropu_by.txt')
    group_by | 'write_group_by' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')
    #
    # wait
    #
    result = p.run()
    result.wait_until_finish()


if __name__ == '__main__':
    main()
