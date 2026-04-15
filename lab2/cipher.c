#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX 1000

//Caesar Cipher

char caesar_encrypt(char ch, int key) {
    if (isupper(ch))
        return (ch - 'A' + key) % 26 + 'A';
    else if (islower(ch))
        return (ch - 'a' + key) % 26 + 'a';
    else
        return ch;
}

char caesar_decrypt(char ch, int key) {
    if (isupper(ch))
        return (ch - 'A' - key + 26) % 26 + 'A';
    else if (islower(ch))
        return (ch - 'a' - key + 26) % 26 + 'a';
    else
        return ch;
}

//Substitution Cipher

char sub_key[] = "QWERTYUIOPASDFGHJKLZXCVBNM";

char sub_encrypt(char ch) {
    if (isupper(ch))
        return sub_key[ch - 'A'];
    else if (islower(ch))
        return tolower(sub_key[ch - 'a']);
    else
        return ch;
}

char sub_decrypt(char ch) {
    char *pos;
    if (isupper(ch)) {
        pos = strchr(sub_key, ch);
        return pos ? 'A' + (pos - sub_key) : ch;
    } else if (islower(ch)) {
        pos = strchr(sub_key, toupper(ch));
        return pos ? 'a' + (pos - sub_key) : ch;
    }
    return ch;
}

int main() {
    FILE *fin, *fout;
    char text[MAX];
    int key = 7;

    fin = fopen("input.txt", "r");
    if (fin == NULL) {
        printf("Error: input.txt not found!\n");
        return 1;
    }

    fgets(text, MAX, fin);
    fclose(fin);

    fout = fopen("output.txt", "w");

    fprintf(fout, "Original Text:\n%s\n\n", text);

    /* Caesar Encryption */
    fprintf(fout, "Caesar Cipher Encryption:\n");
    for (int i = 0; text[i]; i++)
        fputc(caesar_encrypt(text[i], key), fout);

    fprintf(fout, "\n\nCaesar Cipher Decryption:\n");
    for (int i = 0; text[i]; i++)
        fputc(caesar_decrypt(caesar_encrypt(text[i], key), key), fout);

    /* Substitution Encryption */
    fprintf(fout, "\n\nSubstitution Cipher Encryption:\n");
    for (int i = 0; text[i]; i++)
        fputc(sub_encrypt(text[i]), fout);

    fprintf(fout, "\n\nSubstitution Cipher Decryption:\n");
    for (int i = 0; text[i]; i++)
        fputc(sub_decrypt(sub_encrypt(text[i])), fout);

    fclose(fout);

    printf("Encryption and Decryption completed successfully. All results saved in output.txt\n");
    return 0;
}


