import sys

def exit(message="", status=0):
  print(message)
  sys.exit(status)

def error(message):
  print(f"Err: {message}\n")
  exit(1)