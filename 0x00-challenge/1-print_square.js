#!/usr/bin/node

/*
    Print a square with the character #
    
    The size of the square must be the first argument 
    of the program.
*/

// Check if the number of command-line arguments is less than 2
if (process.argv.length <= 2) {
    // Print an error message to the standard error
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./print_square.js <size>\n");
    process.stderr.write("Example: ./print_square.js 8\n");
    process.exit(1); // Exit the program with an error code
}

// Parse the size argument from the command line as an integer
const size = parseInt(process.argv[2]);

// Loop to print the square
for (let i = 0; i < size; i++) {
    // Loop to print each row of the square
    for (let j = 0; j < size; j++) {
        process.stdout.write("#"); // Print a #
    }
    process.stdout.write("\n"); // Move to the next line after each row
}
