# Log Collector

As an application support engineer or a developer, you may need to collect application logs of a particular interval to pinpoint problems in the application. The number of logs can be huge. Log collector is a simple Linux-based tool to collect all files/logs between two particular timestamps and transfer them to a particular folder and zip it. It can also collect files whose names match a regular expression

## Usage

1. Create a file named log_collector.py, copy the contents of the script and save it your Linux machine
2. Run ./log_collector.py without any command-line option. It will display the help message and also examples as to how to run the script.

```
user@Linux:~$ ./log_collector.py 
Usage: log_collector.py [options]

Options:
  -h, --help            show this help message and exit
  --start_date= start date [DD:MM]
  --start_time= start time [hh:mm]
  --end_date= end date [DD:MM]
  --end_time= end time [hh:mm]
  --source_folder= source_folder
  --dest_folder= destination folder
  --pattern= pattern (Will be treated as an ERE)

Example:
./log_collector_v3.py --start_date 20/01 --start_time 16:00 --end_date 01/02 --end_time 13:00 --source_folder /home/user1/test_folder_1 --dest_folder /home/user1/folder_2

./log_collector_v3.py --start_date 20/01 --start_time 16:00 --end_date 01/02 --end_time 13:00 --source_folder /home/user1/test_folder_1 --dest_folder /home/user1/folder_2 --pattern '"\bYOUR_PATTERN_"'


user@Linux:~$ 

```


## Full example

```
# This is the source folder from where a few files need to be copied

user@Linux:~/test_folder_2$ ls -ltra
total 12
--rw-rw-r--  1 user user    0 Jan  1 05:47 file_1
-rw-rw-r--  1 user user    0 Jan  2 05:47 file_2
-rw-rw-r--  1 user user    0 Jan  3 05:47 file_3
-rw-rw-r--  1 user user    0 Jan  4 05:47 file_4
-rw-rw-r--  1 user user    0 Jan  5 05:47 file_5
-rw-rw-r--  1 user user    0 Jan  6 05:47 file_6
-rw-rw-r--  1 user user    0 Jan  7 05:47 file_7
-rw-rw-r--  1 user user    0 Jan  8 05:47 file_8
-rw-rw-r--  1 user user    0 Jan  9 05:47 file_9
-rw-rw-r--  1 user user    0 Jan 20 13:25 file_10
-rw-rw-r--  1 user user    0 Jan 20 14:25 file_11
-rw-rw-r--  1 user user    0 Jan 20 15:25 file_12
-rw-rw-r--  1 user user    0 Jan 20 16:25 file_13
-rw-rw-r--  1 user user    0 Jan 20 17:25 file_14
-rw-rw-r--  1 user user    0 Jan 20 18:25 file_15
-rw-rw-r--  1 user user    0 Jan 29 22:11 file_16
-rw-rw-r--  1 user user    0 Jan 29 22:18 file_21
-rw-rw-r--  1 user user    0 Jan 29 22:24 file_20
-rw-rw-r--  1 user user    0 Jan 29 22:35 file_18
-rw-rw-r--  1 user user    0 Jan 29 22:49 file_17
-rw-rw-r--  1 user user    0 Feb  1 03:05 file_22
-rw-rw-r--  1 user user    0 Feb  1 12:17 file_23
-rw-rw-r--  1 user user    0 Feb  2 06:35 NMSTO_135.bz2
-rw-rw-r--  1 user user    0 Feb  2 14:25 file_24
-rw-rw-r--  1 user user    0 Feb  2 20:29 file_25
-rw-rw-r--  1 user user    0 Feb  3 16:35 NMSTO_136.bz2
-rw-rw-r--  1 user user   30 Feb  6 05:22 file_19
-rw-rw-r--  1 user user    0 Feb 10 12:46 run_NMSTO_138.bz2
-rw-rw-r--  1 user user    0 Feb 10 12:47 NMSTO_137.bz2
-rw-rw-r--  1 user user    0 Feb 15 18:35 run_NMSTO_139.bz2
-rw-rw-r--  1 user user    0 Feb 16 21:00 NMSTO_140.bz2
drwxr-xr-x  2 user user 4096 Mar 31 20:50 .
drwxr-xr-x 58 user user 4096 Apr  5 03:45 ..
user@Linux:~/test_folder_2$ 
user@Linux:~/test_folder_2$ 


# Run the script specifying the start date, start time, end date, end time, source folder and destination folder

user@Linux:~$ ./log_collector.py --start_date 06/01 --start_time 05:00 --end_date 02/02 --end_time 19:00 --source_folder /home/user/test_folder_2 --dest_folder /home/user/test_folder_7

Following files are being copied

file_6
file_7
file_8
file_9
file_10
file_11
file_12
file_13
file_14
file_15
file_16
file_21
file_20
file_18
file_17
file_22
file_23
NMSTO_135.bz2
file_24
file_25

	==========> Logs saved to /tmp/logs_05_04_2018_04_04_48.zip

user@Linux:~$

# If required, one can also specify the regex pattern to copy only those files whose names match a particular pattern

user@Linux:~$ ./log_collector.py --start_date 02/02 --start_time 06:00 --end_date 10/02 --end_time 16:00 --source_folder /home/user/test_folder_2 --dest_folder /home/user/test_folder_7 --pattern '"NMSTO_*"'

Following files are being copied

NMSTO_135.bz2
NMSTO_136.bz2
run_NMSTO_138.bz2
NMSTO_137.bz2
run_NMSTO_139.bz2

	==========> Logs saved to /tmp/logs_05_04_2018_04_28_00.zip

user@Linux:~$
```
