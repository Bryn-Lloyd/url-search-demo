# (C) British Crown Copyright 2017, Met Office
"""
A command-line utility to hit the API endpoint with specific search parameters
in the query string and download all the available files

    Args:
        api-key: The Api-key to access the data

"""
import argparse
import os.path
import time

import requests


START_TIME_STEP = 12
END_TIME_STEP = 36
DOWNLOAD_DIR = 'downloaded_objects'
API_GATEWAY_URL = 'https://api.metoffice.gov.uk/objects/v1/global/data'


def perform_search(api_key):
    # The model reference time for the current date
    current_date = time.strftime('20%y-%m-%d')
    forecast_reference_time = current_date + 'T00:00:00Z'

    # The search parameters to include for diagnostic names
    name = ('rainfall_rate',
            'air_pressure_at_sea_level',
            'wind_speed',
            'wind_from_direction')

    # The time step search parameters (start and end timesteps in seconds)
    start_time = START_TIME_STEP*3600
    end_time = END_TIME_STEP*3600

    # Loop through parameters to find and download available data
    for name_parameter in name:
        for forecast_period in range(start_time, end_time, 3600):
            query_string_parameters = '?name=' + name_parameter + \
                                      '&forecast_reference_time=' \
                                      + forecast_reference_time + \
                                      '&forecast_period=' + \
                                      str(forecast_period)
            search_for_available_files(query_string_parameters, api_key)


def search_for_available_files(query_string, api_key):
    # print('Checking: ' + API_GATEWAY_URL + query_string)
    url_response = requests.get(
        API_GATEWAY_URL + query_string,
        headers={'x-api-key': api_key})
    if 'urls' not in url_response.json():
        print('No urls were found.')
        print(url_response.json())
    else:
        list_of_urls = sorted(url_response.json()['urls'])
        if len(list_of_urls) > 0:
            for url in list_of_urls:
                download(url, api_key)


def download(url, api_key):
    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)
    target_path = os.path.join(DOWNLOAD_DIR,  url.split('/')[-1])
    with open(target_path, 'wb') as file:
        # get request
        response = requests.get(url, headers={'x-api-key': api_key})
        # write to file
        file.write(response.content)
        print('Completed download of {} to {}'.format(url, target_path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Download objects via the API search functionality')
    parser.add_argument('api_key')
    args = parser.parse_args()
    perform_search(args.api_key)
