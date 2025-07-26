
def convert(time):
        hours,minutes = time.split(":") 
        hours = int(hours)
        minutes = int(minutes)
        return hours + minutes/60 



def main ():

    enter_time = input("what time is it? ")
    final_time = convert(enter_time)
    if 7 <= final_time <=8:
        print("breakfast time")
    elif 12 <= final_time <= 13: 
        print("lunch time")
    elif 18 <= final_time <=19: 
        print("dinner time")
    else:
        print(" ")


    
if __name__== "__main__":
    main()