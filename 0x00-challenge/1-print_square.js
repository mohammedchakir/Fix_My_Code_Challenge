#!/usr/bin/node
/*
    Print a square with the character '#'
    
    The size of the square must be the first argument 
    of the program.
*/

// Check if the command line argument is missing
if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1); // Exit the program if the argument is missing
}

// Parse the size argument as an integer (base 10)
let size = parseInt(process.argv[2], 10);

// Loop to create rows of the square
for (let i = 0; i < size; i++) {
    // Loop to create columns of the square
    for (let j = 0; j < size; j++) {
        process.stdout.write("#"); // Print the '#' character
    }
    process.stdout.write("\n"); // Move to the next line after each row
}
