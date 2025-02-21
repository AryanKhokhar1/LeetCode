class Solution(object):
    def isPicked(self, students, sandwiches, i):
        if(i == len(students)):
            return False
        if students[i] == sandwiches[0]:
            students.pop(i)
            sandwiches.pop(0)
            return True
        else:
            return self.isPicked(students,sandwiches,i+1)
    def countStudents(self, students, sandwiches):
        # Behave with students like a queue

        # Behave with sandwiches like a stack
        val = True
        while len(students) > 0 and val:
            val = self.isPicked(students, sandwiches, 0)
        return len(students)