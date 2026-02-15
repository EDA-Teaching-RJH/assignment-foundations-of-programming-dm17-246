
# Assignment 1

**Constraint:** 
You cannot use Dictionaries or Classes (Not yet covered). You must use **Parallel Lists**. You are not permitted to use AI tools to auto-generate code.

## Scenario

You are a new Ensign in the Operations Division. The ship's "Personnel Management System" was written by a developer who has been transferred off the ship for incompetence. The code is a disaster: it is one giant block of over 100 lines, uses global variables incorrectly, contains infinite loops, and crashes constantly.

Your orders are to **refactor the entire codebase** into a modular, function-based system and expand its capabilities to manage the entire crew.

## Part A: The "Spaghetti Code" Disaster (20 Marks)

**Context:** The following code is provided to you. It is a single, massive script with no structure.

**Task:**

1. Open this code space (https://classroom.github.com/a/eVR42nHF) I have populated it with this spaghetti code.
    
2.  Debug the **Syntax Errors** (missing colons, broken strings).
    
3.  Debug the **Logical Errors** (Infinite loops, list index out of range, type errors).
    
4.  **Do not fix the structure yet.** Just get this specific block of code to run without crashing, then save it as `old_system.py`.
    
5.  Document **10 distinct bugs** you found, **you will need this for part C**.

**Each Fix is worth 2 Marks for a maximum of 20 Marks** 

**Hints**

You will want to research the functionality of ``.pop()`` and ``.index()`` 
https://docs.python.org/3/tutorial/datastructures.html

```
🔴🔴🔴 YOU MUST COMMIT EVERYTIME YOU SQUASH A BUG  🔴🔴🔴
```

```python

n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        
    
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt = "1":  
            print("Current Crew List:")
            
            for i in range(10):
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
           
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or "Commander": 
                    count = count + 1
            print("High ranking officers: " + count) 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith
```
```
🔴🔴🔴 YOU MUST COMMIT EVERYTIME YOU SQUASH A BUG  🔴🔴🔴
```
## Part B: The Modular Architecture (40 Marks)

**Context:** You must create a **NEW** file called `fleet_manager.py`. You cannot use the old code structure. You must build a robust system using **Parallel Lists** to track 4 data points per crew member: `Names`, `Ranks`, `Divisions`, and `IDs`.

**Requirements:** You must attempt to implement **ALL 10** of the following functions. Each function must be called correctly from a central `main()` loop. Each function is worth **(4 Marks Each) with a maximum of 40 Marks**

Incomplete = **0 Marks**
Partial Implementation = **2 Marks** 
Full Implementation = **4 Marks**

**Hints** 

 - [ ] Some of the definitions will use multiple variables not just one
       to run, for example ```add_member()``` takes names, ranks, divs
       and ids.        




```
🔴🔴🔴 YOU MUST COMMIT EVERYTIME YOU ADD A FEATURE  🔴🔴🔴
```

1.  `init_database()`: Returns 4 lists pre-populated with at least 5 Star Trek characters and their data.
    
2.  `display_menu()`: Queries users full name, Prints the options and current student logged in and returns the user's choice.
    
3.  `add_member(names, ranks, divs, ids)`:
    
    -   Validates ID is unique.
        
    -   Validates Rank is a valid TNG rank.
        
    -   Appends data to all 4 lists.
        
4.  `remove_member(names, ranks, divs, ids)`:
    
    -   Asks for an ID.
        
    -   Finds the index.
        
    -   Removes the entry from _all 4 lists_ to keep them in sync.
        
5.  `update_rank(names, ranks, ids)`:
    
    -   Finds a member by ID.
        
    -   Updates their rank string.
        
6.  `display_roster(names, ranks, divs, ids)`:
    
    -   Iterates through the lists using `range(len(names))`.
        
    -   Prints a formatted table of all crew.
        
7.  `search_crew(names, ranks, divs, ids)`:
    
    -   Asks for a search term.
        
    -   Prints any crew member whose name contains that term.
        
8.  `filter_by_division(names, divs)`:
    
    -   Asks user for "Command", "Operations", or "Sciences".
        
    -   Prints only members in that division using `match` or `if` .
        
9.  `calculate_payroll(ranks)`:
    
    -   Iterates through the ranks list.
        
    -   Assigns a credit value to ranks (e.g., Captain = 1000, Ensign = 200).
        
    -   Returns the total cost of the crew.
        
10.  `count_officers(ranks)`:
    
	   -   Counts how many "Captain" and "Commander" ranks exist and returns the integer.

```
🔴🔴🔴 YOU MUST COMMIT EVERYTIME YOU ADD A FEATURE  🔴🔴🔴
```

## Part C: The Development Report (25 Marks)

**Length:** 1 Page.

1.  **Legacy Code Post-Mortem:** A breakdown of the 10 bugs found in Part A. You must explain _why_ the bug occurred (e.g., "The code `if x = 1` causes a Syntax Error because `=` is assignment, whereas `==` is comparison" ). **(20 Marks)  2 per bug**
    
2.  **Parallel List Strategy:** Explain the dangers of using parallel lists. What happens if you remove a name from the `names` list but forget to remove the ID from the `ids` list? How did your code prevent this, or how could it be prevented?
 **(5 Marks)**
Incomplete = **0 Marks**
Partial Implementation = **3 Marks** 
Full Implementation = **5 Marks**



## Part D: Technical Demonstration (15 Marks)

**Length:** 3-5 Minutes.

1.  **Refactor Demo:** Show the `old_system.py` crashing, then show your fixed version of it from Part A running. **(5 Marks)** 
Incomplete = **0 Marks**
Partial Implementation = **3 Marks** 
Full Implementation = **5 Marks**


    
3.  **System Tour:** Walk through your new `fleet_manager.py`. **(10 Marks)** Incomplete = **0 Marks**
Partial Implementation = **5 Marks** 
Full Implementation = **10 Marks**



## Model solutions and feedback 
Model solutions will be provided after grades are awarded. Feedback will be attached to Moodle for you to review when grades are released.


## Recording Video 

### Windows
Using the Snipping Tool (for Any Screen Area)

-   **Open Snipping Tool**: Press Windows key + Shift + S, then select the video camera icon, or search "Snipping Tool".

-   **Start New Recording**: Click "New", then drag to select the screen area you want to record.
- **Make sure Mic is enabled**: We need to hear your narration.

-   **Start Recording**: Click the "Start" button for a countdown.

-   **Control & Stop**: Use the pause/resume/stop buttons to manage your recording.

-   **Save Video**: Click the save icon or select "Edit in Clipchamp" to trim and save as MP4.

### Mac

**Methods for Recording Video on Mac:**

-   **QuickTime Player :**
    -   Open QuickTime Player, then choose  `File`  >  `New Movie Recording`.
    -   Click the arrow next to the record button to select microphone, and quality settings
        
        
    
    -   Click the record button to start, and again to stop.
