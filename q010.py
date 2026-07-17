sec=int(input("Enter no. of seconds you want to convert :"))
min=sec//60
remaining_sec=sec%60
hour=min//60
remaining_min=min%60
print(min,"minutes",remaining_sec,"second")
print(hour,'Hours',remaining_min,"min")