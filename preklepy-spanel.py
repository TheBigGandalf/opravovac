input_path = 'syn2015_word_utf8.tsv'

vocabulary = []

def correct_text(text):
  words = text.split(' ')
  for word in words:
    if word not in vocabulary: # TODO optimize
      print(word)
    
def load_vocabulary(path):
  with open(path, 'r') as input_file:
    for line in input_file:
      fields = line.split('\t')
      # word = fields[1]
      rank, word, frequency, _, _, _, _, _ = fields
      vocabulary.append(word)
  
load_vocabulary(input_path)
user_text = input('enter text to correct: ')

correct_text(user_text)
