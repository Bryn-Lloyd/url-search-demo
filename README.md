# URL search and download of model data

Demonstrates downloading model data using URL query string parameters. 

By following these instructions you will be able to hit the API endpoint using an AWS account.
A Python script will query the available data with the supplied query parameters. 
The URLs returned from the query will then be used to download model data.

## Pre-requisites

 - A Python 3 environment
 - Request lib for Python
 - Api-key to access

## Getting started

#### 1. Running the Python
To run the python as a script from a bash command line, simply enter the following:
```
python search_and-download.py YOUR_API_KEY_GOES_HERE
```

#### 2. Tweaking the search parameters

#### Change the model in the url
The model can be altered in the python, simply change ``global`` (in the url) to the required model.
```
20| API_GATEWAY_URL = 'https://api.metoffice.gov.uk/objects/v1/global/data'
```

#### Tweak the timesteps
The timesteps start and end time can be altered in the python.
```
17| START_TIME_STEP = 12
18| END_TIME_STEP = 36
```

#### Edit the diagnostic names
There is currently a list of diagnostic names in the python which can be altered to meet search requirements.
```
29| name = ('rainfall_rate'
30|         'air_pressure_at_sea_level'
31|         'wind_speed'
32|         'wind_from_direction')
``` 

#### 3. Downloading the data
Once the  search parameters have looped over and all available files have been discovered, 
the python will then download the files to a local directory named ``downloaded_objects``.  

#### Debugging
For help debugging, there are various print statements in the python code that only need to be 
uncommented for a better overview of the processes.  

## Authors

* **Bryn Lloyd** - *Initial work* - [Met Office](https://github.com/MetOffice)

See also the list of [contributors](https://github.com/bryn-lloyd/url-search-demo/contributors) who participated in this project.

## License
  
This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
