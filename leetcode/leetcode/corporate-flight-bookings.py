class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flight_seats = [0] * n

        for i in bookings:
            flight_seats[i[0]-1]+=i[2]
            if(i[1]< n):
                flight_seats[i[1]]-=i[2]
        
        for i in range(1,n):
            flight_seats[i] = flight_seats[i - 1] + flight_seats[i]
        
        return flight_seats
