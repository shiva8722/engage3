import pytest
import requests
import pandas as pd
import datatest as dt
from datatest import validate
from engage_script import *

# data validation for required format
@pytest.fixture(scope='module')
@dt.working_directory(__file__)
def df():
    # json_url = 'https://jsonplaceholder.typicode.com/photos'
    # return pd.read_csv('engage_interview.tsv', sep='\t')
    return data_conversion(json_url)

@pytest.mark.mandatory
def test_columns(df):
    dt.validate(
        df.columns,
        {'new_photo_id','title','new_url','timestamp'},
    )

def test_title(df):
    dt.validate(df['title'], str)


def test_new_photo_id(df):
    dt.validate(df['new_photo_id'], str)

def test_new_url(df):
    dt.validate(df['new_url'], str)

iso_8601_format = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9]) (2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
def test_timestamp(df):
    dt.validate.regex(df['timestamp'], iso_8601_format)

