greetings = ("Hey", "Hello", "What's up?", "How are you?")

def filter_Hs(greeting):
  if greeting.startswith('H'): return True
  else: return False
all_H_greetings = tuple(filter(filter_Hs, greetings))

print("All Greetings:", greetings)
print("Greetings Beginning with 'H':", all_H_greetings)