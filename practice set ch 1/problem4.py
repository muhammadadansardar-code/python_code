import os

# Ye line khud hi "C:\Users\Smart ComputerS\Desktop\python" ka rasta bana degi
path = os.path.join(os.path.expanduser("~"), "Desktop", "python")

try:
    # Folder ki list nikalna
    files = os.listdir(path)
    
    print(f"--- '{path}' mein ye files hain ---")
    
    # Ek ek kar ke file ka naam print karna
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")

except FileNotFoundError:
    print("Ghalti: Desktop par 'python' naam ka folder nahi mila.")
    print("Baraye meherbani check karen ke folder ka naam sahi hai.")
except Exception as e:
    print(f"Koi aur masla aa gaya hai: {e}")