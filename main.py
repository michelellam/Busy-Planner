from busy import Get_Busy
import datetime
import json

def openClose(open, close):
    list = []
    for i in range(open, close + 1):
        list.append(i)
    return list

def availableHours(freetime, open_range):
    return (list(set(freetime) & set(open_range)))
        
def perfectHours(available, busy):
    copy_hours = available.copy()
    
    for a in copy_hours:
        for b in busy:
            if a == b:
                available.remove(a)
                
    return available

def changeTime(time):
    if(time == 24):
        return (str(time) + " AM")
    elif(time > 12):
        time -= 12
        return (str(time), " PM")
    else:
        return (str(time), " AM")

def main():
    try:
        place1 = input("Insert the first priority place: ") # Target
        address1 = input("Insert street name and city: ")  # Vestal Parkway East, Vestal
        place2 = input("Insert the second priority place: ") # Wegmans
        address2 = input("Insert street name and city: ") # Harry L Dr, Johnson City
        place3 = input("Insert the third priority place: ") # Red Chili Restaurant
        address3 = input("Insert street name and city: ") # Vestal Parkway East, Vestal
        
        free_from = input("From what time are your free? (military time): ") # 10
        free_to = input("To what time are your free? (military time): ") # 20
        
        if int(free_from) < 1:
            print("Invalid number. Type in between 1 ~ 24.")
            exit(0)
        
        if int(free_to) > 24:
            print("Invalid number. Type in between 1 ~ 24.")
            exit(0)
        
        current_day = datetime.datetime.now()

        freetime_list = []
        for i in range(int(free_from), int(free_to) + 1): # Gets range of free time
            freetime_list.append(i)
        
        venue_list = {
                    (place1, address1),
                    (place2, address2),
                    (place3, address3)
                }
        
        place_w_busy = {}
        place_w_open_close = {}
        list_w_open_close = []
        
        for venue in venue_list:

            params = {
            'api_key_private': 'pri_697d7e59ec3b4ec78ed4d4a79b19ffdd',
            'venue_name': venue[0], # user input, placename
            'venue_address': venue[1], # user input, place address
            'day_int': current_day.day
            }

            busy = Get_Busy(params)

            place_w_busy[venue[0]] = busy.getBusyHrs()
            
            list_w_open_close.append(busy.getOpenHrs())
            list_w_open_close.append(busy.getClosedHrs())
            
            place_w_open_close[venue[0]] = list_w_open_close
         
        priority1_busy = place_w_busy[place1]
        priority2_busy = place_w_busy[place2]      # Get Priority Busy
        priority3_busy = place_w_busy[place3]
        
        priority1_open_close = place_w_open_close[place1]
        priority2_open_close = place_w_open_close[place2]      # Get Priority Open and Close
        priority3_open_close = place_w_open_close[place3]
        
        open_close_range1 = openClose(priority1_open_close[0], priority1_open_close[1])
        open_close_range2 = openClose(priority2_open_close[0], priority2_open_close[1])       # Gets range of open and close
        open_close_range3 = openClose(priority3_open_close[0], priority3_open_close[1])
        
        available_hours1 = availableHours(freetime_list, open_close_range1)
        available_hours2 = availableHours(freetime_list, open_close_range2)           # Get range of available time
        available_hours3 = availableHours(freetime_list, open_close_range3)
        
        perfect_hours1 = perfectHours(available_hours1, priority1_busy)
        perfect_hours2 = perfectHours(available_hours2, priority2_busy)           # Extracts busy hours from available hours
        perfect_hours3 = perfectHours(available_hours3, priority3_busy)
        
        combined_list = []
        combined_list = perfect_hours1 + perfect_hours2 + perfect_hours3 # hrs avail for both priorities
        
        frequency = {}
        for item in combined_list:
            if (item in frequency):
                frequency[item] += 1
            else:
                frequency[item] = 1
        
        p1_dict = {}
        for k in perfect_hours1:
            p1_dict[k] = frequency[k]
        

        final_data = {}

        p1_least_FINAL = min(p1_dict, key=p1_dict.get) # FINAL VALUE FOR P1 (if 9 then 9-10am kinda vibe)
        final_data[place1] = changeTime(p1_least_FINAL)

        combined_list.remove(p1_least_FINAL) #remove picked priority 1 time
        
        new_frequency = {}
        for item in combined_list:
            if (item in new_frequency):
                new_frequency[item] += 1
            else:
                new_frequency[item] = 1
        
        p2_dict = {}
        for m in perfect_hours2:
            p2_dict[m] = new_frequency[m]

        p2_least_FINAL = min(p2_dict, key=p2_dict.get) # FINAL VALUE FOR P2 (if 9 then 9-10am kinda vibe)
        final_data[place2] = changeTime(p2_least_FINAL)

        combined_list.remove(p2_least_FINAL) #remove picked priority 1 time
        
        new2_frequency = {}
        for item in combined_list:
            if (item in new2_frequency):
                new2_frequency[item] += 1
            else:
                new2_frequency[item] = 1
        
        p3_dict = {}
        for y in perfect_hours3:
            p3_dict[y] = new2_frequency[y]

        p3_least_FINAL = min(p3_dict, key=p3_dict.get) # FINAL VALUE FOR P3 (if 9 then 9-10am kinda vibe)
        final_data[place3] = changeTime(p3_least_FINAL)


        output = open("final_times.json", "w")
        json.dump(final_data, output, indent = 3)
        output.close()
                
    except:
        print("Error")
        pass
    
main()