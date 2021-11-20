
from time import sleep
from threading import *


print("")
print("")
process_count = 0
while process_count < 1 or process_count > 5:
    process_count = int(input("Number of processes(Must be between 1-5): "))

print(process_count," Processes initialized")
print("")

if(process_count>=1):
    print("Process 1 Initializing...")
    value_count = int(input("How many values in P1(must be between 1-3): "))
    process1_data = []
    for x in range(value_count):
        print("Enter value at index: ",x)
        process_1 = int(input())
        process1_data.append(process_1) 
print("")
if(process_count>=2):
    print("Process 2 Initializing...")
    value_count2 = int(input("How many values in P2(must be between 1-3): "))
    process2_data = []
    for x in range(value_count2):
        print("Enter value at index: ",x)
        process_2 = int(input())
        process2_data.append(process_2) 
print("")
if(process_count>=3):
    print("Process 3 Initializing...")
    value_count3 = int(input("How many values in P3(must be between 1-3): "))
    process3_data = []
    for x in range(value_count3):
        print("Enter value at index: ",x)
        process_3 = int(input())
        process3_data.append(process_3) 
print("")
if(process_count>=4):
    print("Process 4 Initializing...")
    value_count4 = int(input("How many values in P4(must be between 1-3): "))
    process4_data = []
    for x in range(value_count4):
        print("Enter value at index: ",x)
        process_4 = int(input())
        process4_data.append(process_4) 
print("")
if(process_count>=5):
    print("Process 5 Initializing...")
    value_count5 = int(input("How many values in P5(must be between 1-3): "))
    process5_data = []
    for x in range(value_count5):
        print("Enter value at index: ",x)
        process_5 = int(input())
        process5_data.append(process_5) 
print("")


m = 0
while m < 1 or m > 3:
    m = int(input("Quantum size for above values(must be between 1-3): "))



if process_count>=1:
    print("P1: ",process1_data)
    class P1(Thread):
        def run(self):
            #Instruction_Register holding current positions......
            for i in range(value_count):
                print("")
                print("")
                print("PCB P1")
                print("ID = P1")
                print("Arrival Time = 0")
                print("Starting Time = 0")
                print("Execution Time = ",len(process1_data))
                print("Executed Instruction: ")
                if(m==1):
                    if(i==0):
                        print("P11 -> ",process1_data[i])
                        sleep(1)
                    if(i==1):
                        print("P12 -> ",process1_data[i])
                        sleep(1)
                    if(i==2):
                        print("P13 -> ",process1_data[i])
                        sleep(1)
                if(m==2):
                    if(i==0):
                        print("P11 -> ",process1_data[i])
                        print("P12 -> ",process1_data[i+1])
                        sleep(1)
                    if(i==1):
                        print("P13 -> ",process1_data[i+1])
                        sleep(1)
                if(m==3):
                    if(i==0):
                        print("P11 -> ",process1_data[i])
                        print("P12 -> ",process1_data[i+1])
                        print("P13 -> ",process1_data[i+2])
                        sleep(1)

if process_count>=2:
    print("P2: ",process2_data)
    class P2(Thread):
        def run(self):
            #Instruction_Register holding current positions......
            for i in range(value_count2):
                print("")
                print("")
                print("PCB P2")
                print("ID = P2")
                print("Arrival Time = 1")
                print("Starting Time = ",m)
                print("Execution Time = ",len(process2_data))
                print("Executed Instruction: ")
                
                if(m==1):
                    if(i==0):
                        print("P21 -> ",process2_data[i])
                        sleep(1)
                    if(i==1):
                        print("P22 -> ",process2_data[i])
                        sleep(1)
                    if(i==2):
                        print("P23 -> ",process2_data[i])
                        sleep(1)
                if(m==2):
                    if(i==0):
                        print("P21 -> ",process2_data[i])
                        print("P22 -> ",process2_data[i+1])
                        sleep(1)
                    if(i==1):
                        print("P23 -> ",process2_data[i+1])
                        sleep(1)
                if(m==3):
                    if(i==0):
                        print("P21 -> ",process2_data[i])
                        print("P22 -> ",process2_data[i+1])
                        print("P23 -> ",process2_data[i+2])
                        sleep(1)

if process_count>=3:
    print("P3: ",process3_data)
    class P3(Thread):
        def run(self):
            #Instruction_Register holding current positions......
            for i in range(value_count3):
                print("")
                print("")
                print("PCB P3")
                print("ID = P3")
                print("Arrival Time = 2")
                print("Starting Time = ",m*2)
                print("Execution Time = ",len(process3_data))
                print("Executed Instruction: ")
                if(m==1):
                    if(i==0):
                        print("P31 -> ",process3_data[i])
                        sleep(1)
                    if(i==1):
                        print("P32 -> ",process3_data[i])
                        sleep(1)
                    if(i==2):
                        print("P33 -> ",process3_data[i])
                        sleep(1)
                if(m==2):
                    if(i==0):
                        print("P31 -> ",process3_data[i])
                        print("P32 -> ",process3_data[i+1])
                        sleep(1)
                    if(i==1):
                        print("P33 -> ",process3_data[i+1])
                        sleep(1)
                if(m==3):
                    if(i==0):
                        print("P31 -> ",process3_data[i])
                        print("P32 -> ",process3_data[i+1])
                        print("P33 -> ",process3_data[i+2])
                        sleep(1)

if process_count>=4:
    print("P4: ",process4_data)
    class P4(Thread):
        def run(self):
            #Instruction_Register holding current positions......
            for i in range(value_count4):
                if(m==1):
                    if(i==0):
                        print("P41 -> ",process3_data[i])
                        sleep(1)
                    if(i==1):
                        print("P42 -> ",process3_data[i])
                        sleep(1)
                    if(i==2):
                        print("P43 -> ",process3_data[i])
                        sleep(1)
                if(m==2):
                    if(i==0):
                        print("P41 -> ",process3_data[i])
                        print("P42 -> ",process3_data[i+1])
                        sleep(1)
                    if(i==1):
                        print("P43 -> ",process3_data[i+1])
                        sleep(1)
                if(m==3):
                    if(i==0):
                        print("P41 -> ",process3_data[i])
                        print("P42 -> ",process3_data[i+1])
                        print("P43 -> ",process3_data[i+2])
                        sleep(1)

if process_count>=5:
    print("P5: ",process5_data)
    class P5(Thread):
        def run(self):
            #Instruction_Register holding current positions......
            for i in range(value_count5):
                if(m==1):
                    if(i==0):
                        print("P51 -> ",process3_data[i])
                        sleep(1)
                    if(i==1):
                        print("P52 -> ",process3_data[i])
                        sleep(1)
                    if(i==2):
                        print("P53 -> ",process3_data[i])
                        sleep(1)
                if(m==2):
                    if(i==0):
                        print("P51 -> ",process3_data[i])
                        print("P52 -> ",process3_data[i+1])
                        sleep(1)
                    if(i==1):
                        print("P53 -> ",process3_data[i+1])
                        sleep(1)
                if(m==3):
                    if(i==0):
                        print("P51 -> ",process3_data[i])
                        print("P52 -> ",process3_data[i+1])
                        print("P53 -> ",process3_data[i+2])
                        sleep(1)


    
print("Quantum size is: ",m)
print("")
print("")
print("")
print("PCB Executing...")
print("")

if process_count>=1:
    t1 = P1()
if process_count>=2:
    t2 = P2()
if process_count>=3:
    t3 = P3()
if process_count>=4:
    t4 = P4()
if process_count>=5:
    t5 = P5()

if process_count>=1:
    t1.start()
    sleep(0.2)
if process_count>=2:
    t2.start()
    sleep(0.2)
if process_count>=3:
    t3.start()
    sleep(0.2)
if process_count>=4:
    t4.start()
    sleep(0.2)
if process_count>=5:
    t5.start()

if process_count>=1:
    t1.join()
if process_count>=2:
    t2.join()
if process_count>=3:
    t3.join()
if process_count>=4:
    t4.join()
if process_count>=5:
    t5.join()

print("")
print("PCB completed")
print("")
print("")
# Python3 program for implementation of
# RR scheduling

# Function to find the waiting time
# for all processes
def findWaitingTime(processes, n, bt,
						wt, quantum):
	rem_bt = [0] * n

	# Copy the burst time into rt[]
	for i in range(n):
		rem_bt[i] = bt[i]
	t = 0 # Current time

	# Keep traversing processes in round
	# robin manner until all of them are
	# not done.
	while(1):
		done = True

		# Traverse all processes one by
		# one repeatedly
		for i in range(n):
			
			# If burst time of a process is greater
			# than 0 then only need to process further
			if (rem_bt[i] > 0) :
				done = False # There is a pending process
				
				if (rem_bt[i] > quantum) :
				
					# Increase the value of t i.e. shows
					# how much time a process has been processed
					t += quantum

					# Decrease the burst_time of current
					# process by quantum
					rem_bt[i] -= quantum
				
				# If burst time is smaller than or equal
				# to quantum. Last cycle for this process
				else:
				
					# Increase the value of t i.e. shows
					# how much time a process has been processed
					t = t + rem_bt[i]

					# Waiting time is current time minus
					# time used by this process
					wt[i] = t - bt[i]

					# As the process gets fully executed
					# make its remaining burst time = 0
					rem_bt[i] = 0
				
		# If all processes are done
		if (done == True):
			break
			
# Function to calculate turn around time
def findTurnAroundTime(processes, n, bt, wt, tat):
	
	# Calculating turnaround time
	for i in range(n):
		tat[i] = bt[i] + wt[i]


# Function to calculate average waiting
# and turn-around times.
def findavgTime(processes, n, bt, quantum):
	wt = [0] * n
	tat = [0] * n

	# Function to find waiting time
	# of all processes
	findWaitingTime(processes, n, bt,
						wt, quantum)

	# Function to find turn around time
	# for all processes
	findTurnAroundTime(processes, n, bt,
								wt, tat)

	# Display processes along with all details
	print("Processes Burst Time	 Waiting",
					"Time Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", bt[i],
			"\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
	
# Driver code
if __name__ =="__main__":
    print("")
    print("")
    print("")
    number_process = ["P1","P2","P3"]
    burst_time = [len(process1_data),len(process2_data),len(process3_data)]
findavgTime(number_process, process_count, burst_time, m)
print("")
print("")
print("")

