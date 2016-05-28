package cipher;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Main {
    public static List<Integer> findCharKeys(int desiredOut) {
        List<Integer> solutions = new ArrayList<>();
        for (int key = Byte.MIN_VALUE; key <= Byte.MAX_VALUE; key++) {
            for (int testChar = 0; testChar < 256; testChar++)
                if (testChar - key == desiredOut) solutions.add(key);
        }
        return solutions;
    }
    
    public static Map<Integer, Integer> findCharMap(int desiredOut) {
        Map<Integer, Integer> solutions = new HashMap<Integer, Integer>();
        for (int key = Byte.MIN_VALUE; key <= Byte.MAX_VALUE; key++) {
            for (int testChar = 0; testChar < 256; testChar++)
                if (testChar - key == desiredOut) solutions.put(key, testChar);
        }
        return solutions;
    }

    public static int findChar(int desiredOut, int currentKey) {
        // Correct if the guess - key = desired
        for (int testChar = 0; testChar < 256; testChar++)
            if (testChar - currentKey == desiredOut) return testChar;
        return -1;
        /*
        for (int testChar = 0; testChar < 256; testChar++)
            if ((testChar ^ currentKey) == desiredOut) return testChar;
        return -1;
        */
    }
    
    public static boolean allContain(List<List<Integer>> inList, int desired) {
    	for (int i = 0; i < inList.size(); i++) {
        	if (!(inList.get(i).contains(desired))) return false;
        }
    	return true;
    }

    public static int[] findArray(int[] desiredOut, int currentKey) {
        int[] teststring = new int[desiredOut.length]; //Reserve 30 character spaces
        //For each space, try to find the integer where the key produces the proper output
        
        //            int ret = findChar(output[0], key);
        //            if (!(ret == -1)) System.out.println(""+ret+" "+key+" "+output[0]);

        for (int testIndex = 0; testIndex < desiredOut.length; testIndex++) {
            int res = findChar(desiredOut[testIndex], currentKey);
            if (res == -1) return new int[desiredOut.length]; //Bad return value :) I hate ram...
            else
                teststring[testIndex] = res;
        }
        return teststring;
    }

    public static void main(String args[]) {
        //30 integers (characters) Decimal representation of the encoded byte array but we good
        int[] output = {241, 231, 224, 241, 227, 248, 173, 235, 176, 220, 223, 246, 241, 176, 220, 174, 240, 220, 235, 173, 241, 220, 176, 235, 173, 242, 228, 229, 250, 135};
        List<List<Integer>> solutions = new ArrayList<>();
        for (int i: output) {
        	solutions.add(findCharKeys(i));
        }
        
        //Find overlap
        for (int q = 0; q < solutions.get(0).size(); q++) {
        	int possible = solutions.get(0).get(q);
        	if (!allContain(solutions, possible)) solutions.get(0).remove(possible);
        }
        
        for (int q: solutions.get(0))
        	System.out.println(q);
        /**
        * Brute force 30 characters. Try the first with every possible key, if it works, keep moving with same key
        *   if it doesn't work on the next one, restart with a new key
        * Outer loop should be keys, not characters.
        * 
        * 
        * Here's the deal. I can guess a whole bunch of character/ key combos
        * When one is guessed, I have to find 
        * 
        * Strat: return a list of all the keys, check for overlap between all 30 characters
        */
        
        /*
        for (int key = 0x0; key < Byte.MAX_VALUE; key++) {
            //With each key, test all possible 30 character string combinations
            int[] arrOut =  findArray(output, key);
            if (!(arrOut[0] == 0)) {
                for (int i: arrOut)
                    System.out.print(""+i+", ");
                break;
            }
        }
        */

        /*
        // convert secret text to byte array
        final byte[] secret = "secret".getBytes()

        final byte[] encoded = new byte[secret.length];
        final byte[] decoded = new byte[secret.length];

        // Generate random key (has to be exchanged)
        final byte[] key = new byte[secret.length];
        new SecureRandom().nextBytes(key);

        // Encrypt
        for (int i = 0; i < secret.length; i++) {
            encoded[i] = (byte) (secret[i] ^ key[i]);
        }

        // Decrypt
        for (int i = 0; i < encoded.length; i++) {
            decoded[i] = (byte) (encoded[i] ^ key[i]);
        }
        */
    }
}
