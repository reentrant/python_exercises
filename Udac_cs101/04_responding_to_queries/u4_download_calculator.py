# -*- coding: utf-8 -*-

# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).
#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
from u4_converting_seconds import convert_seconds

def download_time(file_size, size_units, bandwidth, bandwidth_units):
  hours = ''
  minutes = ''
  seconds = ''
  kilobyte = 2 ** 10 * 8
  megabyte = 2 ** 20 * 8
  gigabyte = 2 ** 30 * 8
  terabyte = 2 ** 40 * 8
  if size_units == 'kB':
    file_size_kb = file_size
  elif 'MB' == size_units:
    file_size_kb = 2 ** 10 * file_size
  else:
    pass
  
  if bandwidth_units == 'kB':
    bw_kb = bandwidth * 1.0
  elif 'MB' == bandwidth_units:
    bw_kb = 2.0 ** 10 * bandwidth
  else:
    pass
  #t = size / bandwidth
  secs = file_size_kb / bw_kb
  
  return convert_seconds(secs)


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

#print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

#print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

#print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

#print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

#print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

