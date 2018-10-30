'''
This function is for getting citibike dataset
it will download the dataset into your local PUIDATA folder and print the path of the data file for the convenient to use
Make sure you have your PUIDATA envrionment already set up 
the format of this fucntion should be 
getCitiBikeCSV(datestring)
e.g. datestring='201808'

'''
 
import os
def getCitiBikeCSV(datestring):
    print ("Downloading", datestring)
    ### First I will heck that it is not already there
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.csv"):
        if os.path.isfile(datestring + "-citibike-tripdata.csv"):
            # if in the current dir just move it
            if os.system("mv " + datestring + "-citibike-tripdata.csv " + os.getenv("PUIDATA")):
                print ("Error moving file!, Please check!")
        #otherwise start looking for the zip file
        else:
            if datestring[0:4] in ['2017','2018']:
                if not os.path.isfile(os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.csv.zip"):
                    if not os.path.isfile(datestring + "-citibike-tripdata.csv.zip"):
                        os.system("curl -O https://s3.amazonaws.com/tripdata/" + datestring + "-citibike-tripdata.csv.zip")
                    ###  To move it I use the os.system() functions to run bash commands with arguments
                    os.system("mv " + datestring + "-citibike-tripdata.csv.zip " + os.getenv("PUIDATA"))
                    os.system("unzip " + os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.csv.zip")
                    os.system("mv " + datestring + "-citibike-tripdata.csv " + os.getenv("PUIDATA"))
                ## NOTE: old csv citibike data had a different name structure. 
            else:
                if not os.path.isfile(os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.zip"):
                    if not os.path.isfile(datestring + "-citibike-tripdata.zip"):
                        os.system("curl -O https://s3.amazonaws.com/tripdata/" + datestring + "-citibike-tripdata.zip")
                    ###  To move it I use the os.system() functions to run bash commands with arguments
                    os.system("mv " + datestring + "-citibike-tripdata.zip " + os.getenv("PUIDATA"))
                    os.system("unzip " + os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.zip")
                    os.system("mv " + datestring + "-citibike-tripdata.csv " + os.getenv("PUIDATA"))
    ### One final check:
    if not os.path.isfile(os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.csv"):
        print ("WARNING!!! something is wrong: the file is not there!")

    else:
        print ("file in place, you can continue")
        print ("the path of the file is %s"%(os.getenv("PUIDATA") + "/" + datestring + "-citibike-tripdata.csv"))
