import os
print("Directorio actual:", os.getcwd())
print("Archivos en el directorio:")
for file in os.listdir('.'):
    print(f"  - {file}")