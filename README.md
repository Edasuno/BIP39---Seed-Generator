# BIP 39 SEED GENERATOR

A offline Bitcoin wallet key generator to prioritize maximum security. By operating entirely offline, it eliminates the risk of online threats such as hacking or phishing. Users can generate unique private seed for their Bitcoin wallets in a secure environment, ensuring that sensitive information remains completely isolated from the internet.

>English and portuguese version currently available.
---

#### ⚿ Why you should generate your seed offline

Even though there are several applications that perform this function, in many cases you will be connected to the internet, which is a problem because you must trust your device when generating the keys and also be sure that your network is secure. Therefore, the seeds must always be generated offline and on a trusted device.

---

## How to use

### 📋 Requirements :

    - Python latest version

## Windows

1. **Download the Installer**:  
   - Go to the [official Python website](https://www.python.org).
   - Click on "Downloads" and select the latest version for Windows.

2. **Run the Installer**:  
   - Double-click the downloaded `.exe` file.
   - Check the box **"Add Python to PATH"** (important for running Python from the command line).
   - Choose **"Customize Installation"** if you want specific features or just click **"Install Now"**.


3. **Verify Installation**:  
   - Open the Command Prompt (`Win + R`, type `cmd`, press Enter).
   - Run the command:  
     ```sh
     python --version
     ```


## Mac

1. **Check Pre-installed Version**:  
   - Open the Terminal and run:  
     ```sh
     python3 --version
     ```
   - macOS often comes with Python 2.x or 3.x pre-installed. It's recommended to install the latest version manually.

2. **Download Python**:  
   - Visit the [official Python website](https://www.python.org).
   - Download the latest macOS installer.

3. **Install Python**:  
   - Double-click the `.pkg` file and follow the installation instructions.

4. **Verify Installation**:  
   - Open the Terminal and run:  
     ```sh
     python3 --version
     ```


## Linux

### Using Package Manager
Linux already has python installed by default in most distributions
1. Open the Terminal.
2. Run the following commands (specific to your Linux distribution):

   **Debian/Ubuntu**:
   ```sh
   sudo apt update
   sudo apt install python3

3. **Verify Installation**
 - Open the Terminal and run:
     ```sh
     python3 --version


### How to Run this Seed Generator

- NOTE: Make sure you are on a secure device and only you can see the key. Make sure you are disconnected from the internet.
1. **Open the Terminal**:
   -     On Windows, open CMD or PowerShell. 
   -     On macOS or Linux, open the Terminal.

. 
2. **Navigate to the File Location**:
   - Use the `cd` command to navigate to the folder where your `.py` file is located.
     ```sh
     cd /path_folder
     ```

. 
3. **Run the Python File**:
   - Execute the Python script by typing:
     ```sh
     python3 Seed _Generator.py
     ```  

- The program is simple and just asks you if you want a 12 or 24 words.  
After that, it will give you your seed along with the extended key. You can use it in your wallet like Electrum, BlueWallet and others.
---

#### ₿ How cryptocurrency wallet seed generation works

The process begins with the creation of a random sequence of bits (entropy). The size of this entropy is usually 128, 160, 192, 224, or 256 bits.

Exemple : 

-      11010110101101101011110010101111...


BIP-39 uses entropy as a starting point. This entropy is extended with a checksum, and the resulting total bits are divided into groups of 11 bits, where each group corresponds to a word in the BIP-39 wordlist


To improve integrity and prevent errors in the mnemonic phrase, a checksum of the entropy is calculated. The checksum is a small number of bits derived from the SHA-256 hash of the original entropy. 

- The number of bits in the checksum is equal to 1 bit for every 32 bits of entropy. For example: For 128 bits of entropy, the checksum will be **4 bits.** For 256 bits of entropy, the checksum will be **8 bits**.

So basically the last word is what makes the key unique.

###### Where does the checksum come from?

> The checksum bits are derived from the SHA-256 hash, which produces a sequence of 256 bits with high entropy (cryptographic randomness). This means that any small change in the original entropy will produce a completely different hash due to the behavior of the SHA-256 algorithm.

> It is a good option to check the consistency between the mnemonic phrase and the entropy. If the phrase is changed, even by just one word, the checksum will be invalid. Since the final binary set will be different.

> For 4 bits (12 words) final there are 16 possibilities

>For 8 bits (24 words) we have 256 possibilities



After generating all the bits of the checksum, they are simply concatenated to the binary of the words without the checksum and with that you have access to the addresses and values.
NOTE: Image for illustrative purposes only to demonstrate an Electrum wallet (Source: Electrum Wiki)

![Exemple Electrum wallet](https://upload.wikimedia.org/wikipedia/commons/f/fc/Capture-Electrum.png)

---
#### Why the program does not generate Qrcode and don't have a graphical interface

The idea behind this seed generator for bitcoin wallet is to be as simple as possible, without needing to install more dependencies than the ones you already have in python or needing to do more things to use it. You can just run and use it on your pendrive with tails or on your old computer that you don't connect to the internet and will only use to generate your keys.

It's completely open source so you can see what happens and be sure that none of your keys are being saved and leaked out there.

Many devices and websites have their own key generators, it's true, but some may not be as reliable and even have a long code that makes it difficult to check.

---

#### 📌Version
- 1.0 BETA the first version, but I'm still looking at more features and more possible types of entropy to include.

---

#### ✒️ Authors

> Ed - Project development 

---
#### 🎁 Expressions of gratitude

>Total and a special gratitude to my friend Miriam who encouraged me to make this project available and helped me on how to do it.




