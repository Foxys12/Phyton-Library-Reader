import importlib

while True:
    library = input("Which library functions do you want to see?=")

    if library.lower() == "q":
        break

    try:
        module = importlib.import_module(library)
        all_functions = dir(module)

        print(f"Toplam Eleman Sayısı: {len(all_functions)}\n")

        for func_name in all_functions:
            if not func_name.startswith("__"):
                obj = getattr(module, func_name)
                doc = str(getattr(obj, "__doc__", "")).strip().split("\n")[0]
                print(f"{func_name} -> {doc}")

    except ModuleNotFoundError:
        print(f"There is no library called {library}")
        
        
        

# Explanation
# Line 1: Grab importlib so we can import libraries dynamically using strings.
# Line 3: Keep the script running in a loop until the user wants to quit.
# Line 4: Check if the user typed 'q'—if so, break the loop and exit.
# Line 7: Wrap things in a try block so wrong inputs won't crash the whole script.
# Line 8: Load the requested module dynamically based on user input.
# Line 9: Fetch everything inside the library (functions, classes, variables).
# Line 11: Show how many total items were found in this library.
# Line 13: Loop through each item name one by one.
# Line 14: Clean internal/dunder stuff -names starting with '__'- to keep output clean and understandable.
# Line 15: Get the actual function/object using its name string.
# Line 16: Pull the first line of the docstring to get a quick summary.
# Line 17: Prints the function name right next to its explanation.
# Line 18: Catch the error if someone asks for a library that isn't installed.
# Line 21-22: Let the user know the library doesn't exist and ask again.