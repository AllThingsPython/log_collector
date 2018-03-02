#! /usr/bin/env python

import sys, os, subprocess, optparse, re, shutil

def date_and_time_checker(input_date, input_time):			# Validate user input

	day = input_date.split("/")[0]
	month = input_date.split("/")[1]
	hour = input_time.split(":")[0]
	min = input_time.split(":")[1]

	if int(day) == 0 or int(day) > 31:
		print "Invalid date\n"
		sys.exit(1)

        if int(month) == 0 or int(month) > 12:      
                print "Invalid date\n"
                sys.exit(1)

        if int(hour) > 23 or int(min) > 59:      
                print "Invalid time\n"
                sys.exit(1)


def folder_checker(source_folder, destination_folder):			# Vaidate source and destination folders

	if not os.access(source_folder, os.F_OK):

		print "\n{} folder does not exist\n".format(source_folder)

		sys.exit(1)

	if not os.access(source_folder, os.R_OK):

		print "\n{} folder does not have read permissions\n".format(source_folder)

		sys.exit(1)

	if not os.access(destination_folder, os.F_OK):

		os.mkdir(destination_folder)

		
	if not os.access(destination_folder, os.W_OK) and not os.access(destination_folder, os.X_OK):

		print "\n{} folder does not have write and execute permissions\n".format(destination_folder)

		sys.exit(1)


def timestamp_generator(input_date, input_time):			# Generate numerical timestamp value	

	if int(input_date.split("/")[1]) < 10:

		month = input_date.split("/")[1][1]
	else:
		month = input_date.split("/")[1]
	
	day = input_date.split("/")[0]

	ts = month + day + input_time.split(":")[0] + input_time.split(":")[1]

	return ts


def file_list_generator(start_ts, end_ts, source_folder_path):		# Generate list of files to be copied
	
	month_dict = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov':'11', 'Dec': '12'}

	tmpfile = 'tmpfile_' + str(os.getpid())

	tmpfile_write = open('/tmp/' + tmpfile, 'w')

	os.chdir(source_folder_path)

	subprocess.call('ls -ltra', stdout=tmpfile_write, shell=True)

	tmpfile_write.close()

	###

	tmpfile_2 = 'tmpfile_2_' + str(os.getpid())

	tmpfile_read = open('/tmp/' + tmpfile, 'r')

	tmpfile_read.next()

	tmpfile_2_write = open('/tmp/' + tmpfile_2, 'w')

	for line in tmpfile_read:

		if line.split()[8] != '.' and line.split()[8] != '..':

			line = line.split()[5:9]

			line[0] = month_dict[line[0]]

			if len(line[1]) == 1:
				line[1] = '0' + line[1]

			line[2] = re.sub(':', '', line[2])

			line.append(line[0] + line[1] + line[2])

			line = " ".join(line)

			tmpfile_2_write.write(line + "\n")

	tmpfile_2_write.close()
	tmpfile_read.close()

	###

	tmpfile_2_read = open('/tmp/' + tmpfile_2, 'r')

	file_list = open('/tmp/file_list', 'w')

	for line in tmpfile_2_read:

		if int(line.split()[4]) >= int(start_ts) and int(line.split()[4]) <= int(end_ts):
		
			file_list.write(line.split()[3] + "\n")

		if int(line.split()[4]) > int(end_ts):

			file_list.write(line.split()[3] + "\n")
			break

	file_list.close()
	tmpfile_2_read.close()

	
def copy_files(source_folder_path, destination_folder_path):		# Copy files to location mentioned by user

	os.chdir(source_folder_path)

	file_list = open('/tmp/file_list', 'r')

	for file in file_list:

		shutil.copy2(file.rstrip(), destination_folder_path)

	file_list.close()


def main():								# Main function

        parser = optparse.OptionParser()

	parser.add_option('--start_date', dest="start_date", metavar=' start date')
	parser.add_option('--start_time', dest="start_time", metavar=' start time')
	parser.add_option('--end_date', dest="end_date", metavar=' end date')
	parser.add_option('--end_time', dest="end_time", metavar=' end time')
	parser.add_option('--source_folder', dest="source_folder", metavar=' source_folder')
	parser.add_option('--dest_folder', dest="dest_folder", metavar=' destination folder')

	options, remainder = parser.parse_args()

	if len(sys.argv[1:]) == 0:

		parser.print_help()
		print """
Example:
./log_collector_v3.py --start_date 20/01 --start_time 16:00 --end_date 01/02 --end_time 13:00 --source_folder /home/user1/test_folder_1 --dest_folder /home/user1/folder_2

"""

		sys.exit(1)

	date_and_time_checker(options.start_date, options.start_time)

	date_and_time_checker(options.end_date, options.end_time)

	folder_checker(options.source_folder, options.dest_folder)

	start_timestamp = timestamp_generator(options.start_date, options.start_time)

	end_timestamp = timestamp_generator(options.end_date, options.end_time)

	file_list_generator(start_timestamp, end_timestamp, options.source_folder)

	copy_files(options.source_folder, options.dest_folder)


main()





