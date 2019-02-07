# Software Spend Reporter

A console application that reads in software spend data and outputs a report summarizing that data.

### Prerequisites

Python Version: 2.7

```
brew install python@2
```

### Running the application

First, download this as a zip file and unzip it, then:


Example usage:
```
python ./software_spend_reporter /path/to/inputfile.csv
```
Example using files in the resources folder:
```
python ./software_spend_reporter resources/input_file.csv
```

### Running the tests

There's a bash script to check the input files against their expected outputs.

### Mark the bash script as executable

```
chmod +x test_software_spend_reporter.sh
```

### Running the script

```
./test_software_spend_reporter.sh
```
If all the tests passed you should see: "All test cases passed!"
