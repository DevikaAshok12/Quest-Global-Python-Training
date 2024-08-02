'''Accept N main strings and N sub strings into lists and
 check create a list of numbers of 0s and 1s 
 where 0 represents that the sub string at respective index is not a substring of the main string.'''
N = int(input("Enter the number of strings: "))
main_list = []
sub_list = []

print("Enter the main strings:")
for _ in range(N):
    main_list.append(input())

print("Enter the sub strings:")
for _ in range(N):
    sub_list.append(input())
presence = []
for i in range(N):
    if sub_list[i] in main_list[i]:
        presence.append(1)
    else:
        presence.append(0)
print(f"Presence: {presence}")