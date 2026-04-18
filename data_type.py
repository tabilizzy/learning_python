'''
checking for data types
'''

def check_manual(val):
      # Boolean check (Strict identity)
      if val is True or val is False:
          return "bool"

      # String check (Behavioral)
      try:
          val + ""
          return "str"
      except: pass

      # Integer check (Unique bitwise behavior)
      try:
          val << 1
          return "int"
      except: pass

      # Complex check (Numeric but non-scalar)
      try:
          if val.imag != 0:
              return "complex"
      except: pass

      # Float check (Numeric but fails integer bitwise shift)
      try:
          val + 0.0
          return "float"
      except: pass

      return "unknown"



print(check_manual(True))
print(check_manual("hello"))
#print(check_manual(2i+j))
print(check_manual(9.5))
print(check_manual(98))



