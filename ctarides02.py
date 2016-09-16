# ctarides.py

'''
The file Data/ctarail.csv contains a history
of CTA "L" ridership from January 1, 2001 to
December 31, 2012. The data looks like this:

station_id,stationname,date,daytype,rides
40010,Austin-Forest Park,01/01/2001,U,290
40020,Harlem-Lake,01/01/2001,U,633
40030,Pulaski-Lake,01/01/2001,U,483
40040,Quincy/Wells,01/01/2001,U,374
40050,Davis,01/01/2001,U,804

The "station_id" column contains a station ID code,
"stationname" is the name of the station,
"daytype" is one of "U" (Sunday/Holiday),
"A" (Saturday), or "W" (Weekday), and the
"rides" column contains the number of passengers
that entered the turnstiles at that station.

Your task is as follows. In a file ctarides.py,
define a function yearly_rides(filename, year)
that simply tabulates the total number of rides
for a given year.
'''

import csv

def yearly_rides(filename, year):
    with open(filename, 'r') as fh:
        reader = csv.reader(fh)
        print(next(reader))    # header row
        counter = 0
        for line in reader:
            if line[2][-4:] == str(year):
                #print(line)
                counter += int(line[4])
    return counter

'''
{
   'station_id' : 40010,                    # Integer
   'station_name' : 'Austin-Forest Park',   # String
   'date' : '01/01/2001',                   # String
   'daytype' : 'U',                         # String
   'rides' : 290                            # Integer
}
'''
def read_rides(filename):
    with open(filename, 'r') as fh:
        reader = csv.reader(fh)
        headers = next(reader)    # header row
        result = []
        for line in reader:
            # transform each line of reader into desired data types
            data_types = [int, str, str, str, int]
            line_in_desired_data_types = [func(field) for func, field in zip(data_types, line)]
            d = dict(zip(headers, line_in_desired_data_types))
            result.append(d)

    return result

if __name__ == '__main__':
    print('2001 : ', yearly_rides('Data/ctarail.csv', 2001))
    print('2002 : ', yearly_rides('Data/ctarail.csv', 2002))
    rides = read_rides('Data/ctarail.csv')
    print(len(rides))
    print(rides[:4])
