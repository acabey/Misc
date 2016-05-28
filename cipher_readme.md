The problem uses a one-way cipher, which will encode your plaintext in a couple different ways. See here: http://www.cimt.plymouth.ac.uk/resources/codes/codes_u12_text.pdf

Since the problem says that it is substitution, the ciphertext (bytes) + the corresponding key (bytes) should be equal to the plaintext (bytes)

I tried to approach the problem in a number of ways, finally giving in

The strat should be to:
  Test all possible keys:
    With every key, find if for the 30 output chars you can generate plaintext
    If the key can be used to generate plaintext which, when encrypted with the key produces the proper output, it is correct
  Print out the String casted plaintext array...
