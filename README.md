# Test-Environment

### API Folder
    RandomFox.py : Basic knowledge of how to use APIs

    BinancePingTest.py : Ping test between your device and binance server. Prints out difference also
    
    BincnaceTest.py : Accessing binance paper trading environment using API.

### CSV Folder
    CSV Files : 2D List of [DATE, VALUE]

    CSVReader.py : Testing enviornment for CSVReader Jupyter notebook

    CSVReader.ipynb : Revised version of CSVReader.py with comments and figures

### JSONreader.py

    JSON reader is another version of the CSV reader.
    Data is populated to the code via json format taken from yahoo stock exchange information.
    This will then be converted into readable data and imported into the code to consistently produce graphs.

    Currently the json format includes previous market data in a dict format
        {'x' : Time in unix (UTC conversion needed), 'y': Value in USD ($)}
    
    TODO
    create UTC conversion function
    integrate the JSON reader into the jupyter