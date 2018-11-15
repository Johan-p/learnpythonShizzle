def censor(text,word):
  wordlen = len(word)
  list = text.split()
  letter = len(list) - 1
  
  while letter >= 0:
    if list[letter] == word:
      list[letter] = "*" * wordlen 
    letter = letter - 1
  return " ".join(list)