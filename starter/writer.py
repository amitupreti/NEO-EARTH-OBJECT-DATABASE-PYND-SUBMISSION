from enum import Enum
import csv


class OutputFormat(Enum):
    """
    Enum representing supported output formatting options for search results.
    """
    display = 'display'
    csv_file = 'csv_file'

    @staticmethod
    def list():
        """
        :return: list of string representations of OutputFormat enums
        """
        return list(map(lambda output: output.value, OutputFormat))


class NEOWriter(object):
    """
    Python object use to write the results from supported output formatting options.
    """

    def __init__(self):
        pass

    def write(self, format, data, **kwargs):
        """
        Generic write interface that, depending on the OutputFormat selected calls the
        appropriate instance write function

        :param format: str representing the OutputFormat
        :param data: collection of NearEarthObject or OrbitPath results
        :param kwargs: Additional attributes used for formatting output e.g. filename
        :return: bool representing if write successful or not
        """

        if format == OutputFormat.display.value:

            print("OK")
            value = list(data[0].__dict__.keys())
            for val in value:
                print('{:<25}'.format(val[:24]), end='')
            print()

            for items in data:
                curr_items = [d for d in items.__dict__.values()]
                for item in curr_items:
                    if isinstance(item, list):
                        item = item[0].__dict__
                        del item['neo_name']
                        item = ', '.join([f'{k}:{v}' for k, v in item.items()])

                    print('{:<25}'.format(item), end='')
                print()

            return True

        if format == OutputFormat.csv_file.value:
            print("Outputting to CSV")
            keys = list(data[0].__dict__.keys())
            with open('output.csv', 'w') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                for dd in data:
                    items = [d for d in dd.__dict__.values()]
                    items[-1] = ', '.join([f'{k}:{v}' for k,
                                           v in items[-1][0].__dict__.items()])

                    writer.writerow(dd.__dict__)
            return True
