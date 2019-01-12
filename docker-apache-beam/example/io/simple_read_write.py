import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
import csv
import io
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))
PATH_TO_DATA_DIR = os.path.abspath(os.path.join(PATH_TO_THIS_DIR, '..', 'sample_data'))


def read_from_csv(p, path, skip_header_lines=True):

    class ReadFromCSV(beam.DoFn):

        def process(self, element):
            row = [r for r in csv.reader([element])]
            return row

    return (p
            | beam.io.ReadFromText(
                path,
                skip_header_lines=skip_header_lines)
            | beam.ParDo(ReadFromCSV()))


def write_to_csv(p, path, skip_header_lines=True):

    class WriteToCSV(beam.DoFn):

        def process(self, element):
            with io.BytesIO() as output:
                writer = csv.writer(output)
                writer.writerow(element)
                d = output.getvalue().strip('\r\n')
                return [d]

    return (p
            | beam.ParDo(WriteToCSV())
            | beam.io.WriteToText(path, file_name_suffix='.csv'))


def main():
    with beam.Pipeline(options=pipeline_options.PipelineOptions()) as p:
        #
        # create
        #
        p_create = p | 'create' >> beam.Create([1, 2, 3])
        path_output = os.path.join(PATH_TO_THIS_DIR, 'foobar.txt')
        p_create | beam.io.WriteToText(path_output, file_name_suffix='.csv')

        #
        # read from csv
        #
        path_csv = os.path.join(PATH_TO_DATA_DIR, 'sample.csv')
        p_csv = read_from_csv(p, path_csv)
        path_output = os.path.join(PATH_TO_THIS_DIR, 'read_csv.txt')
        p_csv | 'write_csv' >> beam.io.WriteToText(path_output, file_name_suffix='.csv')


if __name__ == '__main__':
    main()
