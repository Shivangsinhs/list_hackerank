# Define the main function
if __name__ == '__main__':
    # Get the number of operations
    N = int(input())
    
    # Initialize an empty list to store the data
    datalist = []
    
    # Loop through the operations
    for i in range(N):
        # Get the current operation
        x = input().split()
        
        # Check the type of operation
        if x[0] == 'insert':
            # Insert the element at the specified index
            datalist.insert(int(x[1]), int(x[2]))
        elif x[0] == 'print':
            # Print the current list
             print(datalist)
        elif x[0] == 'remove':
            # Remove the first occurrence of the specified element
            datalist.remove(int(x[1]))
        elif x[0] == 'append':
            # Append the element to the end of the list
            datalist.append(int(x[1]))
        elif x[0] == 'sort':
            # Sort the list in ascending order
            datalist.sort()
        elif x[0] == 'pop':
            # Remove the last element from the list
            datalist.pop()
        elif x[0] == 'reverse':
            # Reverse the order of elements in the list
            datalist.reverse()
