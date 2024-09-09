


def reverse_word():
  Sur_name = "Nnanna"
  first_name = "Mari"
  Total_name = (Sur_name)[::-1] + " " + (first_name)[::-1] 
  
  return Total_name


print(reverse_word())

def Name(sur_name, first_name):
  return sur_name[::-1] +  first_name[::-1]
  
print(Name("Nnanna", "Mari"))

# def reverse_string(s):
#   if " " in s:
#     return (s.split())[::-1][0] + "_" + (s.split())[::-1][1]
#   else:
#     return s[::-1]


# print(reverse_string("hello"))  # "olleh"
# print(reverse_string("this team"))  # "meat_sith"

def whatever(name):
  return name[::-1]


print(whatever("hello"))  
