def nums(l1,l2):
        j1 = ''
        j2 = '' 
        while True:
                if l1 != []:
                        j1 = j1+str(l1.pop())
                elif l2 !=[]:
                        j2 = j2+str(l2.pop())
                else:
                        break

        result = str(int(j1) + int(j2))
        lens = len(str(result))
        results = []

        for i in range(lens):
                results.append(int(result[i]))

        results = list(reversed(results))
        return results



l1 = [9,9,9,9]
l2 = [9,9,9,9,9,9,9]
print(nums(l1,l2))
