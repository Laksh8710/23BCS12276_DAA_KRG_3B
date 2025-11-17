class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        j = 0  
        m = len(passengers)
        last_boarded_times = [] 
        for bus in buses:
            count = 0
            while j < m and passengers[j] <= bus and count < capacity:
                last_boarded_times.append(passengers[j])
                j += 1
                count += 1
            if bus != buses[-1]:
                last_boarded_times = []
        passenger_set = set(passengers)

        if len(last_boarded_times) < capacity:
            t = buses[-1]
        else:
            t = last_boarded_times[-1] - 1
        while t in passenger_set:
            t -= 1
        return t

