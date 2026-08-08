package main
import "fmt"
import "sort"

type Process struct{
	id string
	arrivalTime int
	burstTime int
	completionTime int
	turnaroundTime int
	waitingTime int
}

func fcfs(processes []Process){
	sort.Slice(processes, func(i,j int) bool{
		return processes[i].arrivalTime < processes[j].arrivalTime
	})

	currentTime := 0

	totalWaiting := 0
	totalTurnaround := 0

	for i :=0; i< len(processes); i++{
		if currentTime<processes[i].arrivalTime{
			currentTime = processes[i].arrivalTime
				
		}
		
		currentTime += processes[i].burstTime
		
		processes[i].completionTime = currentTime
		processes[i].turnaroundTime = processes[i].completionTime - processes[i].arrivalTime
		processes[i].waitingTime = processes[i].turnaroundTime - processes[i].burstTime
		totalWaiting += processes[i].waitingTime
		totalTurnaround += processes[i].turnaroundTime
		
	}
	fmt.Printf("\nAverage Waiting Time: %.2f\n", float64(totalWaiting)/float64(len(processes)))
	fmt.Printf("Average Turnaround Time: %.2f\n", float64(totalTurnaround)/float64(len(processes)))

	fmt.Println("\nGantt Chart:")

	currentTime = 0

	for i := 0; i < len(processes); i++ {

    	if currentTime < processes[i].arrivalTime {
        	fmt.Printf("%d | Idle | ", currentTime)
        	currentTime = processes[i].arrivalTime
    	}

    	fmt.Printf("%d | %s | ", currentTime, processes[i].id)

    	currentTime += processes[i].burstTime
	}

	fmt.Println(currentTime)
}


func sjf(processes []Process) {
    n := len(processes)

    done := make([]bool, n)

    currentTime := 0
    completed := 0

    totalWaiting := 0
    totalTurnaround := 0

    fmt.Println("\nGantt Chart:")

    for completed < n {

        chosen := -1

        // find the shortest process which has already arrived
        for i := 0; i < n; i++ {

            
            if done[i] {
                continue
            }
	    if processes[i].arrivalTime > currentTime {
                continue
            }
	    if chosen == -1 {
                chosen = i
                continue
            }
	    if processes[i].burstTime < processes[chosen].burstTime {
                chosen = i
            }
        }

        
        if chosen == -1 {
            currentTime++
            continue
        }

        fmt.Printf("%d | %s | ", currentTime, processes[chosen].id)

        currentTime += processes[chosen].burstTime

        processes[chosen].completionTime = currentTime
        processes[chosen].turnaroundTime = processes[chosen].completionTime - processes[chosen].arrivalTime
        processes[chosen].waitingTime = processes[chosen].turnaroundTime - processes[chosen].burstTime

        totalWaiting += processes[chosen].waitingTime
        totalTurnaround += processes[chosen].turnaroundTime

        done[chosen] = true
        completed++
    }

    fmt.Println(currentTime)

    fmt.Printf("\nAverage Waiting Time: %.2f\n",float64(totalWaiting)/float64(n))

    fmt.Printf("Average Turnaround Time: %.2f\n",float64(totalTurnaround)/float64(n))
}

func roundRobin(processes []Process, quantum int) {
    n := len(processes)

    sort.Slice(processes, func(i, j int) bool {
        return processes[i].arrivalTime < processes[j].arrivalTime
    })

    remaining := make([]int, n)

    for i := 0; i < n; i++ {
        remaining[i] = processes[i].burstTime
    }

    queue := []int{}

    currentTime := 0
    nextProcess := 0
    completed := 0

    totalWaiting := 0
    totalTurnaround := 0

    fmt.Println("\nGantt Chart:")

    for completed < n {

        if len(queue) == 0 {
            if currentTime < processes[nextProcess].arrivalTime {
                fmt.Printf("%d | Idle | ", currentTime)
                currentTime = processes[nextProcess].arrivalTime
            }

            queue = append(queue, nextProcess)
            nextProcess++
        }

         chosen := queue[0]
        queue = queue[1:]

        runTime := quantum

        if remaining[chosen] < quantum {
            runTime = remaining[chosen]
        }

        fmt.Printf("%d | %s | ", currentTime, processes[chosen].id)

        currentTime += runTime
        remaining[chosen] -= runTime

       
        for nextProcess < n &&
            processes[nextProcess].arrivalTime <= currentTime {

            queue = append(queue, nextProcess)
            nextProcess++
        }

        
        if remaining[chosen] > 0 {
            queue = append(queue, chosen)
        } else {
            processes[chosen].completionTime = currentTime

            processes[chosen].turnaroundTime = processes[chosen].completionTime - processes[chosen].arrivalTime

            processes[chosen].waitingTime = processes[chosen].turnaroundTime - processes[chosen].burstTime

            totalWaiting += processes[chosen].waitingTime
            totalTurnaround += processes[chosen].turnaroundTime

            completed++
        }
    }

    fmt.Println(currentTime)

    fmt.Printf("\nAverage Waiting Time: %.2f\n",float64(totalWaiting)/float64(n))

    fmt.Printf("Average Turnaround Time: %.2f\n",float64(totalTurnaround)/float64(n))
}


func main(){
	var n int
	fmt.Print("Enter number of Process: ")
	fmt.Scan(&n)

	processes := make([]Process, n)
	
	for i := 0; i<n; i++{
		fmt.Println("\nProcess", i+1)
		
		fmt.Println("Process ID: ")
		fmt.Scan(&processes[i].id)
		
		fmt.Print("Arrival Time: ")
		fmt.Scan(&processes[i].arrivalTime)

		fmt.Print("Burst Time: ")
		fmt.Scan(&processes[i].burstTime)


	
	}
	var input int
	fmt.Println("Choose the CPU Scheduling Algorithm\n")
	fmt.Println("FCFS : PRESS 1\nSJF : PRESS 2\nROUND ROBIN : PRESS 3\n")

	fmt.Scan(&input)
	if input == 1{
		fcfs(processes)
	}
	if input == 2{
		sjf(processes)
	}
	if input ==3{
		var QT int
		fmt.Println("Enter the Quant Time")
		fmt.Scan(&QT)
		roundRobin(processes,QT)
	}

	fmt.Println("\nProcesses: ")

	fmt.Println("\nPID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")

	for i := 0; i < n; i++ {
    	fmt.Printf("P%s\t%d\t%d\t%d\t\t%d\t\t%d\n",
        	processes[i].id,
        	processes[i].arrivalTime,
        	processes[i].burstTime,
        	processes[i].completionTime,
        	processes[i].turnaroundTime,
        	processes[i].waitingTime,
    	)
	}
	

}
