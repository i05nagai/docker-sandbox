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
    # An example of simple join (i.e. CoGroupByKey)
    #
    p = beam.Pipeline(options=pipeline_options.PipelineOptions())
    #
    # email
    #
    emails_list = [
        ('amy', 'amy@example.com'),
        ('carl', 'carl@example.com'),
        ('julia', 'julia@example.com'),
        ('carl', 'carl@email.com'),
    ]
    path_output = os.path.join(PATH_TO_THIS_DIR, 'emails.txt')
    emails = p | 'create_emails' >> beam.Create(emails_list)
    emails | 'write_emails' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')
    #
    # phones
    #
    phones_list = [
        ('amy', '111-222-3333'),
        ('james', '222-333-4444'),
        ('amy', '333-444-5555'),
        ('carl', '444-555-6666'),
    ]
    phones = p | 'create_phones' >> beam.Create(phones_list)
    path_output = os.path.join(PATH_TO_THIS_DIR, 'phones.txt')
    phones | 'write_phones' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')
    #
    # join
    #
    joined = ({'emails': emails, 'phones': phones}
              | beam.CoGroupByKey())
    path_output = os.path.join(PATH_TO_THIS_DIR, 'joined.txt')
    joined | 'write_joined' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')
    #
    # wait
    #
    result = p.run()
    result.wait_until_finish()


if __name__ == '__main__':
    main()
