class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st, sum = [], 0
        for i in range(len(operations)):
            if operations[i] == "+":
                num = st[-1] + st[-2]
                st.append(num)
            elif operations[i] == "D":
                num = st[-1] * 2
                st.append(num)
            elif operations[i] == "C":
                st.pop()
            else:
                st.append(int(operations[i]))
            print(st)
        while bool(st):
            sum += st.pop()

        return int(sum)