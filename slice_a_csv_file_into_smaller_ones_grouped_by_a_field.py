__author__ = 'rich'

"""
    You could use a regular csv reader and writer,
    but the DictReader and DictWriter are nice
    because you can reference columns by name.

    Always use the 'b' flag when reading or writing .csv
    files because on Windows that makes a difference in
    how line-endings are handled.
"""
import csv, itertools as it, operator as op

csv_contents = []
with open('Data/world_bank_data.csv', 'rb') as fin:
  dict_reader = csv.DictReader(fin)   # default delimiter is comma
  fieldnames = dict_reader.fieldnames # save for writing
  for line in dict_reader:            # read in all of your data
    csv_contents.append(line)         # gather data into a list (of dicts)

# input to itertools.groupby must be sorted by the grouping value
sorted_csv_contents = sorted(csv_contents, key=op.itemgetter('Country Name'))

for groupkey, groupdata in it.groupby(sorted_csv_contents,
                                      key=op.itemgetter('Country Name')):
  with open('tmp/slice_{:s}.csv'.format(groupkey), 'wb') as fou:
    dict_writer = csv.DictWriter(fou, fieldnames=fieldnames)
    dict_writer.writeheader()         # new method in 2.7; use writerow() in 2.6-
    dict_writer.writerows(groupdata)