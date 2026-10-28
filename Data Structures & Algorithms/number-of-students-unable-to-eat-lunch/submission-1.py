class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        index = 0
        res = n
        for sandwich in sandwiches:
            count = 0
            while count < n and students[index] != sandwich:
                index += 1
                index %= n
                count += 1
            if students[index] == sandwich:
                students[index] = -1
                res -= 1
            else:
                break
        return res