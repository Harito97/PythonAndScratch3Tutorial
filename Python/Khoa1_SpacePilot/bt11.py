"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""

if __name__ == "__main__":
    filename = input(
        "Input the filename and it's extension: "
    )  # filename = foae.wh.faq.dowfe -> extension là dowfe
    slice_filename = filename.split(".")
    if len(slice_filename) < 2:
        print("The file has no extension.")
    else:
        print(
            "The extension of the file is: " + slice_filename[-1].lower()
        )  # quy ước là mọi phần mở rộng của 1 file đều viết thường
