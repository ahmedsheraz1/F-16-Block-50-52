Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
        filtered_data

        
[56.2]
[56.2, 51.7]
[56.2, 51.7, 55.3]
[56.2, 51.7, 55.3, 52.5]
[56.2, 51.7, 55.3, 52.5, 47.8]
