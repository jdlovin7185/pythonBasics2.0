def tower_of_hanoi(n, source, destination, temp):
    if n == 1:
        # removes the element in the specified position
        disk = source.pop(0)
        destination.insert(0, disk)
        return
    tower_of_hanoi(n-1, source, temp, destination)
    disk = source.pop(0)
    destination.insert(0, disk)
    tower_of_hanoi(n - 1, temp, destination, source)
    return


source = ["blue", "green", "orange"]
destination = []
temp = []
tower_of_hanoi(3, source, destination, temp)
print("Source", source)
print("Destination", destination)
