from pathlib import Path

root = Path(r"D:\VISIONPROJECT")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"{root.name}\n")

    for item in sorted(root.iterdir()):
        f.write(f"├── {item.name}\n")

        if item.is_dir():
            for subitem in sorted(item.iterdir()):
                f.write(f"│   ├── {subitem.name}\n")

print("Tree saved to output.txt")