from collections.abc import MutableMapping, MutableSequence
from decimal import Decimal


class PrimitiveKVFormatter(object):

    def format_kv(self, key, value):
        """
        Format key value pair as text
        :type key: str
        :param key: the dict element key name in string
        :type value: (bool, int, float, Decimal, str)
        :param value: the primitive value
        :rtype: str
        :return: formatted key value in text
        """
        if value:
            if isinstance(value, bool):
                return f'{{"{key}":"{str(value).lower()}"}}'
            elif isinstance(value, str):
                return f'{{"{key}":"{value}"}}'
            elif isinstance(value, int) or isinstance(value, float):
                return f'{{"{key}":{value}}}'
            elif isinstance(value, Decimal):
                v = f'{value.normalize():f}'
                return f'{{"{key}":{v}}}'
            else:
                raise ValueError("Non-primitive type")
        else:
            return f'{{"{key}":null}}'


class TextUtils(object):

    def __init__(self):
        pass

    @staticmethod
    def flatten_dict(input_dict,
                     formatter=PrimitiveKVFormatter(),
                     key_joiner='.',
                     array_index_start=0,
                     array_index_prefix='$'):
        """
        Flatten nested dict object.

        :type input_dict: :class:`~MutableMapping`
        :param input_dict: the nested dict to flatten
        :type formatter: :class:`~PrimitiveKVFormatter`
        :param formatter: key value formatter
        :type key_joiner: str
        :param key_joiner: joiner between multi level keys
        :type array_index_start: int
        :param array_index_start: the start index of array element, 0 by default
        :type array_index_prefix: str
        :param array_index_prefix: prefix for array element index
        :rtype: str
        :return: flatten text
        :raise: :class:`~ValueError`
        """
        if isinstance(input_dict, MutableMapping):
            if input_dict:
                queue = list(input_dict.items())
                result = list()
                while queue:
                    key, val = queue.pop(0)
                    if val and isinstance(val, MutableMapping):
                        for sub_key, sub_val in val.items():
                            queue.append((f'{key}{key_joiner}{sub_key}', sub_val))
                    elif val and isinstance(val, MutableSequence):
                        for index, item in enumerate(val, start=array_index_start):
                            if item and isinstance(item, MutableMapping):
                                queue.append((f'{key}{key_joiner}{array_index_prefix}{index}', item))
                            elif item and isinstance(item, MutableSequence):
                                queue.append((f'{key}{key_joiner}{array_index_prefix}{index}', item))
                            else:
                                result.append(formatter.format_kv(f'{key}{key_joiner}{array_index_prefix}{index}', item))
                    else:
                        result.append(formatter.format_kv(key, val))
                return ','.join(result)
            else:
                return None
        elif input_dict is None:
            return None
        else:
            raise ValueError("Invalid value")
