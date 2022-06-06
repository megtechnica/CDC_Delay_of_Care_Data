import pandas as pd
from validation import type_check_numeric_columns, compare_nulls_against_threshold
from isolation import isolate_total_stub, isolate_age_stub
from visualization import plot_visualization


# very simple extraction, drop some columns and check some data
cdc_data = pd.read_csv('CDC_Delay_of_Care_Data.csv')
cdc_data = cdc_data.drop(columns=['INDICATOR','FLAG','UNIT'])


# do you have good data?
data_types_valid = type_check_numeric_columns(cdc_data)
acceptable_null_threshold = compare_nulls_against_threshold(cdc_data)


if (data_types_valid[1] == True) and (acceptable_null_threshold == True):
    pass
elif (data_types_valid[1] == False):
    raise TypeError("Girl you got the wrong type in this column: " + data_types_valid[0])
elif (acceptable_null_threshold == False):
    raise ValueError("There are too many nulls in this data")

# separate the categories of delayed care
delay_of_medical_care = cdc_data[cdc_data.PANEL == 'Delay or nonreceipt of needed medical care due to cost']
delay_of_pharm_care = cdc_data[cdc_data.PANEL == 'Nonreceipt of needed prescription drugs due to cost']
delay_of_dental_care = cdc_data[cdc_data.PANEL == 'Nonreceipt of needed dental care due to cost']

# isolate the totals stub
total_delay_of_medical_care = isolate_total_stub(delay_of_medical_care)
total_delay_of_pharm_care = isolate_total_stub(delay_of_pharm_care)
total_delay_of_dental_care = isolate_total_stub(delay_of_dental_care)

# plot the graph
plot_visualization(total_delay_of_medical_care)
plot_visualization(total_delay_of_dental_care)
plot_visualization(total_delay_of_pharm_care)
