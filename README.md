
# A Solution to Data Engineering Coding Challenge

## How to Run
- Install the packages in the requirement.txt
- create a **config.ini** file as per the **config.template** and place it in config folder
e.g. 
```sh
[FILE]
SPEC_FILE = ./fixed-width/spec.json
NO_OF_RECORDS = 10
FIXED_WIDTH_FILE = ./fixed-width/sample_fixed_width_file.txt
CSV_FILE = ./fixed-width/sample_csv_output.csv
DELIMITER = |
```
- run the main file

**NOTE** The fixed width file generator adds 2 whitespaces to each feild and breakline at the end of each record to make the output more readable.
