# -*- coding: utf-8 -*-
import pandas as pd
from decimal import Decimal
from text_utils import PrimitiveKVFormatter, TextUtils

# https://www.gairuo.com/file/data/dataset/GDP-China.csv


df = pd.DataFrame({
    "id": [1, 2],
    "name": ["Kevin", "Jenny"],
    "address": [{"hometown": "Meizhou", "work": "Guangzhou"}, {"hometown": "Hangzhou", "work": "Guangzhou"}],
    "contact": [{"mobile": ["+86 16888", "+86 168888"], "mail": "niceman@nice.lab"},
                {"mobile": ["+86 16666", "+86 166666"], "mail": "nicelady@nice.lab"}],
    "magic": [Decimal('000001.10000010'), Decimal('000002.20000020')]
})

df['contact'] = df['contact'].apply(
    lambda c: TextUtils.flatten_dict(c, formatter=PrimitiveKVFormatter(), array_index_start=1))

with pd.option_context("expand_frame_repr", False,
                       "display.max_rows", None,
                       "display.max_colwidth", None):
    print(df)
