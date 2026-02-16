
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
    
2.  **Parallel List Strategy:** Explain the dangers of using parallel lists. What happens if you remove a name from the `names` list but forget to remove the ID from the `ids` list? How did your code prevent this, or how could it be prevented? **(5 Marks)**
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

# Part C – Development Report
## 1. Legacy Code Post-Mortem

### Bug 1 – Incorrect Comparison Operator

The original code used:

`if opt = "1":`

This caused a SyntaxError because `=` is used for assignment, not comparison. In conditional statements, `==` must be used to compare values. This was corrected to:

`if opt == "1":`

### Bug 2 – Function Not Being Called

The function `run_system_monolith` was defined but not executed correctly. Writing the function name without parentheses does not run the function. For example:

`run_system_monolith`

This does nothing. The function must be called using parentheses:

`run_system_monolith()`

Without this, the program does not start properly.

### Bug 3 – Infinite Loop in Loading Section

The original code contained a loop:

`while loading < 5:`

Inside the loop, the value of `loading` was never incremented. This caused an infinite loop because the condition always remained true. The fix was to add:

`loading += 1`

This allowed the loop to progress and eventually stop.

### Bug 4 – List Index Out of Range

The code used:

`for i in range(10):`

However, the lists only contained four elements. This caused an `IndexError` because the loop attempted to access indices that did not exist. The issue was fixed by replacing it with:

`for i in range(len(n)):`

This ensures the loop only iterates through valid indices.

### Bug 5 – String and Integer Concatenation Error

The original code attempted to print:

`print("High ranking officers: " + count)`

This caused a `TypeError` because `count` is an integer and cannot be directly concatenated with a string. The fix was to convert the integer to a string:

`print("High ranking officers: " + str(count))`

This ensures both values are strings before concatenation.

### Bug 6 – Incorrect Logical Condition

The original condition was written as:

`if rank == "Captain" or "Commander":`

This always evaluates as True because the string `"Commander"` is a non-empty value, which is considered True in Python. As a result, the condition did not work correctly.

The fix was to explicitly compare both conditions:

`if rank == "Captain" or rank == "Commander":`

This ensures the comparison is evaluated properly.

### Bug 7 – Removing a Non-Existent Element

The original code used:

`idx = n.index(rem)`

If the name was not in the list, this caused a `ValueError` because `.index()` cannot find a value that does not exist.

The fix was to first check whether the name exists:

`if rem in n:`

This prevents the program from crashing and ensures safe removal.

### Bug 8 – Parallel Lists Becoming Misaligned

In the original version, when adding a new crew member, only the name was appended to the list:

`n.append(new_name)`

However, the corresponding rank and division were not added to their lists. This caused the parallel lists to become misaligned, meaning the indices no longer matched correctly.

To fix this, I made sure to append the new data to all related lists at the same time. This keeps the parallel structure consistent and prevents incorrect data mapping.

### Bug 9 – Whitespace Causing Input Mismatch

While testing the remove feature, I noticed that entering extra spaces before or after a name caused the system to not find the member, even though the name existed.

This happened because user input included hidden whitespace characters.

To solve this, I used `.strip()` when reading input. This removes unnecessary spaces and ensures the comparison works correctly.

### Bug 10 – Lack of Input Validation

The original system did not validate user input properly. This meant that invalid ranks or unexpected values could be entered without any checks.

This could lead to inconsistent data and logical errors later in the program.

In my fix, I added validation checks for ranks and divisions to ensure only allowed values are accepted. If the input is invalid, the system now prints an error message and prevents incorrect data from being added.

## 2. Parallel List Strategy

Parallel lists store related data in separate lists, but they rely on index alignment. This means the data at index 0 in the `names` list must match index 0 in the `ranks`, `divisions`, and `ids` lists.

If one list is modified without updating the others, the system becomes inconsistent. For example, if a name is removed but the corresponding ID is not removed, the data will no longer match correctly.

In my implementation, I prevented this by always finding the correct index first and then removing or updating all lists using the same index. This keeps the structure synchronized.

Although parallel lists work for small systems, using classes or dictionaries would be safer in larger applications.

