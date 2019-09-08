# Driver Data
> utilizing the python command line, this program ingests a raw txt file and outputs Driver: {miles} mile $ {mph} mph to the terminal sorted by miles driven


### Technologies Used
> python 3.6.3


### Troubleshooting
> If errors are immediately thrown, ensure you are running python 3.6. To determine this, you can run the following in the terminal
```
which python
 OR
which python3
```

### Run Program
```
python3 main.py <file.txt>
```

### Run Unittests
tests are written using the unittest library which is part of the Python standard library
```
python3 -m unittest -v tests
```

### Design
Effectively organized data to find all drivers within the dataset and use the driver's firstname as the key in a  driver meta hashmap.
When iterating through each line of the raw text field, control flow off first word of each line and appending each trip's
data to the driver within the hashmap as an array or arrays or create a new key and append the data. This breaks down if there are two unique drivers with the same
firstname, however, my assumption is that each driver's name is a unique hash.
