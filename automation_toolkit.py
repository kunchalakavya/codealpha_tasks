import os
import shutil
import tempfile
import pandas as pd

# -----------------------------
# 1. File Organizer
# -----------------------------
def organize_files(target_folder):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xls', '.xlsx'],
        'Audio': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css'],
        'Others': []
    }

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for folder, extensions in file_types.items():
                if ext in extensions:
                    dest_folder = os.path.join(target_folder, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(target_folder, 'Others')
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))

    print("✅ File organization complete.\n")

# -----------------------------
# 2. Data Cleaner
# -----------------------------
def clean_csv_data(file_path):
    try:
        df = pd.read_csv(file_path)
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        # Auto-clean: convert all string columns to lowercase
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].str.lower()

        cleaned_file = "cleaned_" + os.path.basename(file_path)
        df.to_csv(cleaned_file, index=False)
        print(f"✅ Data cleaned and saved as '{cleaned_file}'.\n")
    except Exception as e:
        print(f"❌ Error cleaning file: {e}")

# -----------------------------
# 3. Temp File Cleaner
# -----------------------------
def clean_temp_files():
    temp_dir = tempfile.gettempdir()
    deleted = 0
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                deleted += 1
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                deleted += 1
        except Exception as e:
            print(f"⚠️ Could not delete {file_path}: {e}")
    print(f"✅ Deleted {deleted} temporary files/folders.\n")

# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:
        print("\n🛠️ Python Task Automation Toolkit")
        print("1. Organize files in a folder")
        print("2. Clean a CSV file")
        print("3. Clean system temporary files")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            folder = input("Enter the full path of the folder to organize: ")
            organize_files(folder)
        elif choice == '2':
            csv_file = input("Enter the full path of the CSV file to clean: ")
            clean_csv_data(csv_file)
        elif choice == '3':
            clean_temp_files()
        elif choice == '4':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
