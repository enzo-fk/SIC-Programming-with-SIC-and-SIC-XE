MEMORY_SIZE = 16 * 1024  # 16 KB
memory = ['00'] * MEMORY_SIZE  # Initialize memory with '00'

def load_object_code(object_code):
    lines = object_code.strip().split('\n')
    # Get the original start address from the header record
    original_start_address = int(lines[0][7:13], 16)
    highest_address = original_start_address  # Initialize highest address as the start address

    # First, find the highest address that will be written to
    for line in lines[1:]:  # Exclude the header record
        if line.startswith('T'):
            start_address = int(line[1:7], 16)
            length = int(line[7:9], 16) * 2  # Length of the object code in characters
            highest_address = max(highest_address, start_address + length // 2 - 1)

    # Calculate the relocation offset
    relocation_offset = MEMORY_SIZE - highest_address - 1
    if relocation_offset < 0:
        raise ValueError("Object code exceeds the memory size.")

    # Relocate the object code
    for line in lines[1:]:  # Exclude the header record
        if line.startswith('T'):
            start_address = int(line[1:7], 16) + relocation_offset
            code = line[9:].strip()
            for i in range(0, len(code), 2):
                memory[start_address + i // 2] = code[i:i+2]


def write_memory_image_file(memory, file_path, program_name="ICOPY"):
    # Find the first and last non-'00' values to determine the actual program size
    start_address = next((index for index, byte in enumerate(memory) if byte != '00'), None)
    end_address = len(memory) - next((index for index, byte in enumerate(reversed(memory)) if byte != '00'), -1)

    with open(file_path, 'w') as file:
        # Write the header line with program name, starting address, program size, and ending address
        file.write(f"{program_name} {start_address:06X}{(end_address - start_address):06X}{end_address:06X}\n")

        # Write the memory contents
        for i in range(start_address, end_address, 32):
            line_bytes = memory[i:i+32]
            # Replace '00' with 'FF', pad with 'FF' if the line is shorter than 32 bytes
            line = ''.join(byte if byte != '00' else 'FF' for byte in line_bytes).ljust(64, 'F').upper()
            file.write(line + '\n')




# Your object code as a string
object_code = """
HCOPY  00100000107A
T0010001E1410334820390010362810303010154820613C100300102A0C103900102D
T00101E150C10364820610810334C0000454F46000003000000
T0020391E041030001030E0205D30203FD8205D2810303020575490392C205E38203F
T0020571C1010364C0000F1001000041030E02079302064509039DC20792C1036
T002073073820644C000005
E001000
"""

load_object_code(object_code)
write_memory_image_file(memory, 'memory_image.txt')

# For debugging: print out a portion of the memory to check if the code is loaded correctly
for i in range(MEMORY_SIZE - 300, MEMORY_SIZE):  # Just as an example
    print(f"{i:04X}: {memory[i]}")

