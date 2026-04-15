#include <stdio.h>
#include <math.h>

// Function to compute gcd
int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

// Function to find modular inverse
int modInverse(int e, int phi) {
    int d;
    for (d = 1; d < phi; d++) {
        if ((d * e) % phi == 1)
            return d;
    }
    return -1;
}

// Power function with mod
long long powerMod(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        result = (result * base) % mod;
        exp--;
    }
    return result;
}

int main() {
    int p, q, n, phi, e, d;
    long long msg, enc, dec;

    // Input prime numbers
    printf("Enter first prime number (p): ");
    scanf("%d", &p);
    printf("Enter second prime number (q): ");
    scanf("%d", &q);

    // Key generation
    n = p * q;
    phi = (p - 1) * (q - 1);

    // Choose public key e
    for (e = 2; e < phi; e++) {
        if (gcd(e, phi) == 1)
            break;
    }

    // Compute private key d
    d = modInverse(e, phi);

    printf("\nPublic Key  (e, n): (%d, %d)", e, n);
    printf("\nPrivate Key (d, n): (%d, %d)\n", d, n);

    // Input message
    printf("\nEnter plaintext (integer): ");
    scanf("%lld", &msg);

    // Encryption
    enc = powerMod(msg, e, n);
    printf("Encrypted ciphertext: %lld\n", enc);

    // Decryption
    dec = powerMod(enc, d, n);
    printf("Decrypted plaintext: %lld\n", dec);

    return 0;
}

