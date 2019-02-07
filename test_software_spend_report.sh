#!/bin/bash

if diff -q <(python software_spend_report.py resources/input_file.csv) <(cat resources/expected_output) &&
diff -q <(python software_spend_report.py resources/input_file_decimal.csv) <(cat resources/expected_output_decimal) &&
diff -q <(python software_spend_report.py resources/input_file_random_order.csv) <(cat resources/expected_output_random_order) &&
diff <(python software_spend_report.py resources/input_file_unconventional_names.csv) <(cat resources/expected_output_unconventional_names); then
echo "All test cases passed!"
else
echo "Eh oh something's wrong"
fi