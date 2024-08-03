#count the number of deletions required to ensure no two adjacent characters are the same

def min_deletions_to_avoid_adjacent_repeats(number_of_queries, strings):
    for str in strings:
        number_of_deletions=0
        for i in range(1,len(str)):
            if str[i] == str[i-1]:
                number_of_deletions+=1
        print(number_of_deletions)
    

number_of_queries = int(input("Enter the number of queries:"))

strings = []
print(f'Enter {number_of_queries} number of querie(s) with A and B')
for i in range(number_of_queries):
    strings.append(input())
print('For each queries miminum number of deletion required is :')

min_deletions_to_avoid_adjacent_repeats(number_of_queries, strings)


        

            
    