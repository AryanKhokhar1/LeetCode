class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count_seats = [0]*(max(seats)+1)
        count_students = [0]*(max(students)+1)
        n = len(seats)
        for i in range(n):
            count_seats[seats[i]] += 1
            count_students[students[i]] +=1
        for i in range(1,len(count_seats)):
            count_seats[i] += count_seats[i-1]
        for i in range(1,len(count_students)):
            count_students[i] += count_students[i-1]
        sorted_seats = [0]*len(seats)
        sorted_students = [0]*len(students)
        for i in range(len(seats)):
            fseats = count_seats[seats[i]] -1
            count_seats[seats[i]] -= 1
            fstudents = count_students[students[i]] -1
            count_students[students[i]] -= 1
            sorted_seats[fseats] = seats[i]
            sorted_students[fstudents] = students[i]
        ans = 0 
        for i in range(len(seats)):
            ans += abs(sorted_students[i] - sorted_seats[i] )
        return ans
