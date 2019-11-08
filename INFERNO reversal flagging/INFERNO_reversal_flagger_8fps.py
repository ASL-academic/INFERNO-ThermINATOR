########INFERNO reversal flagger with batch processing functionality########

import math,re,decimal,os #import python modules used later in script


########commented block start########
#This code block initializes some variables used within the code
count = 0
time=[]
x_coord=[]
y_coord=[]
x_4frame_average=[]
y_4frame_average=[]
angle_diff_vector=[]
angle_change=[]
track_id=[]
track=0
viable=[]
reversal=[]
max_frame=0
total_events=[]
count_tracks=0
binned_reversal_rate=[]
binned_reversal=[]
binned_noevent=[]
binned_total_events=[]
folder_path = './blobs/' 
########commented block end########



for data_file in os.listdir(folder_path): #line starts a loop, each pass loading data_file with the name of one input blob file from the /blobs subdirectory  
    print data_file #status screen printout to know which input file the script is currently processing
########commented block start########
#For each pass of the for loop, this code block re-initializes some variables used within the code and sets paths for input/output files   
    folder_path = './blobs/'
    count = 0
    time=[]
    x_coord=[]
    y_coord=[]
    x_4frame_average=[]
    y_4frame_average=[]
    angle_diff_vector=[]
    angle_change=[]
    track_id=[]
    track=0
    viable=[]
    reversal=[]
    max_frame=0
    total_events=[]
    count_tracks=0
    binned_reversal_rate=[]
    binned_reversal=[]
    binned_noevent=[]
    binned_total_events=[]
    data_file_in=folder_path+data_file #path generation for current input .blobs file
    data_file_out=folder_path+data_file.replace('.blobs','.txt') #path generation for current output .txt file
    outfile = open (data_file_out,'w') #open a new output file in write mode
########commented block end########

    with open(data_file_in) as f: #open current input file
        for line in f: #go through each line of the input file
            if line.startswith("%"): #identify where a new worm track begins; sample MWT track header: %1473
                track= line.rstrip() #store track from the line
            else:
                value = line.split() #split the line into a list, using any whitespace as a separator; store the result in value
                if (len(value)>10): #select only lines which contain skeletonized worm data (i.e. list must have more than 10 elements)
                    track_id.append(track) #store track for current line as a new element in list
                    time.append(float(value[1])) #store timepoint (in seconds) for current line as a new element in list
                    x_coord.append(float(value[2])) #store the x-axis coordinate for current line as a new element in list
                    y_coord.append(float(value[3])) #store the y-axis coordinate for current line as a new element in list

                    count += 1 #keep track of the total number of lines containing usable coordinate data

    max_frame = int(max(time) * 8)  #converts the maximum time value in the list(end of experimental recording) into frames (recording FPS = 8)

    for i in range(0,count): #go through each positional index 
        if (i>=4) and (track_id[i]==track_id[i-4]): #conditional branch checking that worm track has been maintained for at least 5 frames (True)
            x_4frame_average.append(sum(x_coord[i-4:i])/4) #store a 4-frame average of the x-axis coordinate 
            y_4frame_average.append(sum(y_coord[i-4:i])/4) #store a 4-frame average of the y-axis coordinate

########commented block start########
#The angle between the difference vector (connecting the vectors at frames i and i-4) and the x-axis was calculated using the 2-argument arctangent function
            if (x_4frame_average[i]-x_4frame_average[i-4]==0) and (y_4frame_average[i]<=y_4frame_average[i-4]):
                angle_diff_vector.append(-math.pi)
            else:
                angle_diff_vector.append(math.atan2(y_4frame_average[i]-y_4frame_average[i-4],x_4frame_average[i]-x_4frame_average[i-4]))
########commented block end########

        else: #conditional branch checking that worm track has been maintained for at least 5 frames (False)
            x_4frame_average.append(0)
            y_4frame_average.append(0)
            angle_diff_vector.append(0)    


    for i in range(0,count): #go through each positional index
        if (i>=10) and (i<count-4) and (track_id[i]==track_id[i-10]):  #conditional branch checking that worm track has been maintained for at least 11 frames (True) 

########commented block start########
#The directed angle change between difference vectors at frames i and i+4 was calculated
            if (math.fabs(angle_diff_vector[i]-angle_diff_vector[i+4])>math.pi):
                angle_change.append(math.fabs(angle_diff_vector[i]-angle_diff_vector[i+4])-2*math.pi)
            else:
                angle_change.append(angle_diff_vector[i]-angle_diff_vector[i+4])
########commented block end########
        else: #conditional branch checking that worm track has been maintained for at least 11 frames (False) 
            angle_change.append(0)


    for i in range(0,count): #go through each positional index
        if (count>i+11) and (track_id[i]!=track_id[i-1]) and (track_id[i]==track_id[i+11]):
            count_tracks += 1 #count total number of worm tracks


########commented block start########
#check if worm has been tracked for long enough and that it will still be tracked for at least 11 more frames.
        if (count>i+11):
            if (track_id[i]==track_id[i-7]) and (track_id[i]==track_id[i+11]): 
                viable.append(1)
            else:
                viable.append(0)
        else:
            viable.append(0)
########commented block end########

        if viable[i]==1: #worms tracked long enough to proceed with reversal scoring                                                                                                                                             
            if (math.fabs(angle_change[i])>2.4) and (track_id[i]==track_id[i-7]) and (count>i+11) and (track_id[i]==track_id[i+11]): #conditional branch identifying reversals when angle change is larger than |2.4 rad| (True)
                
                reversal.append(1) #flag a reversal event (1) at current index position         
            else: #conditional branch identifying reversals when angle change is larger than |2.4 rad| (False)
                reversal.append(0) #flag no event (0) at current index position
        else: #worms not tracked long enough to proceed with reversal scoring
            reversal.append(-1) #flag unviable (-1) index position


    print 'Number of worm tracks in file:'
    print count_tracks
    print 'Reversal flagging done!'
    print 'Generating output files...'



#intended datastructure for reversal_matrix:
#   -1 for frames where the track is not covered
#    0 for frames where reversal=0
#    1 for frames where reversal=1
    reversal_matrix = [[-1 for x in range(0,count_tracks+1)] for y in range(0,max_frame+1)] #initialize a xy matrix with -1, where the x-axis spans all worm tracks and the y-axis spans all frames in recording   
    reversal_track = 0

    for i in range(0,count): #go through each positional index
        reversal_matrix[int(time[i]*8)][reversal_track]=reversal[i] #populate reversal_matrix with reversal data obtained earlier
        if (count>i+11) and (track_id[i]!=track_id[i-1]) and (i>=1) and (track_id[i]==track_id[i+11]): #identify when worm track changes 
            reversal_track += 1 #increment track index by 1

    reversal_binned_matrix = [[-1 for x in range(0,count_tracks+1)] for y in range(0,(max_frame/32+2))] #initialize a xy matrix with -1, where x-axis spans all worm tracks and y-axis spans 4 second bins in recording
    reversal_binned_track = 0 
    reversal_binned_time = 0
    acquisition_switch=0
    reversal_switch=0

########commented block start########
#This block of code compresses the reversal_matrix into 4 second bins. 
#intended datastructure for reversal_binned_matrix:
#   -1 for 4 second bins where the worm is not tracked
#    0 for 4 second bins where the worm is tracked, but no reversals were flagged 
#    1 for 4 second bins where the worm is tracked and at least one reversal was flagged
    for x in range (0,count_tracks+1):  #go through original, uncompressed reversal_matrix
        for y in range (0,max_frame+1): #go through original, uncompressed reversal_matrix
            if (reversal_matrix[y][x]==0): 
                acquisition_switch = 1 #triggered at timepoint if current worm track has started worm movement acquisition
            if (reversal_matrix[y][x]==1):
                reversal_switch = 1 #triggered at timepoint if current worm track has flagged a reversal event

         
            if (y%32==0): #checks when the time index has counted up to 32 frames (4 seconds with 8 FPS recording)
                if (acquisition_switch!=1) and (reversal_switch!=1): #
                    reversal_binned_matrix[reversal_binned_time][reversal_binned_track]=-1 #if worm is not tracked and no reversals are found, flag the current 4s bin as -1
                    if (reversal_binned_time<max_frame/32):  
                        reversal_binned_time += 1 #if the end of recording is not yet reached, go to the next 4 second bin
                    else:
                        reversal_binned_time=0      #if the end of the recording is reached, reset time to start of movie
                        reversal_binned_track += 1  #and go to the next worm track
                    acquisition_switch = 0 #before going to next bin, reset worm movement acquisition switch          
                    reversal_switch = 0    #before going to next bin, reset worm reversal flagging switch
                if (acquisition_switch==1) and (reversal_switch!=1):
                    reversal_binned_matrix[reversal_binned_time][reversal_binned_track]=0 #if worm is tracked and no reversals are found, flag the current 4s bin as 0
                    if (reversal_binned_time<max_frame/32): 
                        reversal_binned_time += 1 #if the end of recording is not yet reached, go to the next 4 second bin
                    else:
                        reversal_binned_time=0      #if the end of the recording is reached, reset time to start of movie
                        reversal_binned_track += 1  #and go to the next worm track
                    acquisition_switch = 0 #before going to next bin, reset worm movement acquisition switch
                    reversal_switch = 0    #before going to next bin, reset worm reversal flagging switch
                if (acquisition_switch!=1) and (reversal_switch==1):
                    reversal_binned_matrix[reversal_binned_time][reversal_binned_track]=-1 #if worm is not tracked and reversals are found, flag the current 4s bin as -1 (failsafe edge case scenario, should not be triggered with normal use)
                    if (reversal_binned_time<max_frame/32):
                        reversal_binned_time += 1 #if the end of recording is not yet reached, go to the next 4 second bin
                    else:
                        reversal_binned_time=0      #if the end of the recording is reached, reset time to start of movie
                        reversal_binned_track += 1  #and go to the next worm track
                    acquisition_switch = 0 #before going to next bin, reset worm movement acquisition switch
                    reversal_switch = 0    #before going to next bin, reset worm reversal flagging switch
                if (acquisition_switch==1) and (reversal_switch==1):
                    reversal_binned_matrix[reversal_binned_time][reversal_binned_track]=1 #if worm is tracked and at least one reversal is found, flag the current 4s bin as 1
                    if (reversal_binned_time<max_frame/32):
                        reversal_binned_time += 1 #if the end of recording is not yet reached, go to the next 4 second bin
                    else:
                        reversal_binned_time=0      #if the end of the recording is reached, reset time to start of movie
                        reversal_binned_track += 1  #and go to the next worm track   
                    acquisition_switch = 0 #before going to next bin, reset worm movement acquisition switch
                    reversal_switch = 0    #before going to next bin, reset worm reversal flagging switch   
########commented block end########


########commented block start########
#This code block generates a population level summary of the reversal_binned_matrix
    for x in range (0, count_tracks+1):      #go through reversal_binned_matrix        
        for y in range (0,max_frame/32+1):   #go through reversal_binned_matrix
            binned_reversal.append(0)
            binned_noevent.append(0)
            binned_reversal_rate.append(0)
            binned_total_events.append(0)
            if reversal_binned_matrix[y][x]==1:
                binned_reversal[y]+=1 #count all reversals at time bin y
            if reversal_binned_matrix[y][x]==0:
                binned_noevent[y]+=1 #count all noevents at time bin y
            if reversal_binned_matrix[y][x]>=0:
                binned_total_events[y]+=1 #count reversals + noevents at time bin y

    for i in range (0,max_frame/32+2):
        if binned_total_events[i]!=0:                      
            binned_reversal_rate[i]=float(binned_reversal[i])/float(binned_total_events[i])*100 #generate a reversal rate (%) at time bin i
        else:
            binned_reversal_rate[i]='DIV0' #edge case when no worms are tracked             
########commented block end########
         
         
########commented block start########
#This block of code generates the output .txt file
    for x in range(0,max_frame/32+1):
        outfile.write (str(binned_reversal[x])) #generate first line of output text; list total number of reversals at each 4 second binning interval
        outfile.write (' ') #whitespace separating each 4 second bin
    outfile.write('\n') #new line 

    for x in range(0,max_frame/32+1): 
        outfile.write (str(binned_noevent[x])) #generate second line of output text; list total number of noevents at each 4 second binning interval
        outfile.write (' ') #whitespace separating each 4 second bin
    outfile.write('\n') #new line

    for x in range(0,max_frame/32+1): 
        outfile.write (str(binned_total_events[x])) #generate third line of output text; list total number of events at each 4 second binning interval
        outfile.write (' ') #whitespace separating each 4 second bin
    outfile.write('\n') #new line

    for x in range(0,max_frame/32+1):
        outfile.write (str(binned_reversal_rate[x])) #generate fourth line of output text; list reversal rate (%) at each 4 second binning interval
        outfile.write (' ') #whitespace separating each 4 second bin
    outfile.write('\n') #new line
    outfile.write('\n') #new line

    for x in range(0,count_tracks+1):
        for y in range(0,max_frame/32+1):
            outfile.write (str(reversal_binned_matrix[y][x])) #generate all subsequent lines of output text, consisting of the reversal_binned_matrix
            if y == max_frame/32:                             #
                outfile.write ('\n')                          #
            else:                                             #
                outfile.write (' ')                           #
########commented block end########
    print '#######################################done############################################# \n \n' 


    outfile.close() #close current output file handle

