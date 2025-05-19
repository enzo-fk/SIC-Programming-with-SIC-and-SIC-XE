README
1. The Python code contains two parts, one to relocate the code, and one to generate the memory_image.txt file.
2. The default relocated address/relocation offset set is 2000, however you can change it in the code by changing the relocation_offset variable in line 46.
3. You can change the object code used by changing the object coded in line 37 of the code. However, make sure the the format of the object code is specified correctly.
4. You can change the header record for the memory image file for the Name and initial letter by changing the program_name parameter in the write_memory_image_file function.
5. After running the code, a memory image txt file will be generated in the directory of your python code. Paste the memory image file generated into the VM Share Folder and open your WinXP Virtual Box Environment you created.
6. Assuming you already have all the tools and setup prepared, including the SIC simulator executable (.exe) file and other related files, copy the memory image file into the directory of the SIC simulator executable file and rename it into "DEVF2".
7. Run the SIC simulator executable file and press L to run the Load command and load the file. Then press R to run the code.

Special Notes:
1. The object file required to use is the one from Page 49 of the textbook, however as I have found the code to be unable to run in the SIC simulator, I decided to paste the memory image file code in the homework doc but use the Hello world code to demonstrate how the relocated code can be run
2. I am unable to find the correct format to be able to run the relocated code, however I am certain the procedure and process of relocating the code is already correct