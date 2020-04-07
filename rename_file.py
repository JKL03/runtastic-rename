import sys
import os
import glob
import gpxpy

# inupt
path = sys.argv[1]

# preparation
saved_cwd = os.getcwd()
os.chdir(path)

# get files
files = glob.glob(os.path.join(path, '*.gpx'))
file_num = 0

# processing
for filename in files:
    gpx = gpxpy.parse(open(filename))
    try:
        os.rename(filename, os.path.join(path, gpx.name + '.gpx'))
    except FileExistsError as e:
        os.rename(filename, os.path.join(path, gpx.name + '1' + '.gpx'))


# clean up
os.chdir(saved_cwd)
print('done')
