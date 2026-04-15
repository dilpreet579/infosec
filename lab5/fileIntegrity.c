#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void generate_hash(const char *filename, const char *hashfile) {
    char command[200];
    
    // Generate SHA-256 hash and store in file
    sprintf(command, "sha256sum %s > %s", filename, hashfile);
    system(command);
}

int compare_hashes(const char *file1, const char *file2) {
    char ch1, ch2;
    FILE *f1 = fopen(file1, "r");
    FILE *f2 = fopen(file2, "r");

    if (!f1 || !f2) {
        printf("Error opening hash files\n");
        return -1;
    }

    while ((ch1 = fgetc(f1)) != EOF && (ch2 = fgetc(f2)) != EOF) {
        if (ch1 != ch2) {
            fclose(f1);
            fclose(f2);
            return 0; // Not equal
        }
    }

    fclose(f1);
    fclose(f2);
    return 1; // Equal
}

int main() {
    char filename[100];

    printf("Enter file name to monitor: ");
    scanf("%s", filename);

    // Step 1: Generate initial hash
    generate_hash(filename, "hash1.txt");
    printf("Initial hash stored in hash1.txt\n");

    printf("Modify the file and press Enter to continue...");
    getchar(); // consume newline
    getchar(); // wait for Enter

    // Step 2: Generate new hash
    generate_hash(filename, "hash2.txt");
    printf("New hash stored in hash2.txt\n");

    // Step 3: Compare hashes
    int result = compare_hashes("hash1.txt", "hash2.txt");

    if (result == 1)
        printf("File Integrity: NOT MODIFIED\n");
    else
        printf("File Integrity: MODIFIED\n");

    return 0;
}
