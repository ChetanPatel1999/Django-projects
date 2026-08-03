from django.test import TestCase

# Create your tests here.
def data(**d):
    for key in d:
        print(f"{key}: {d[key]}")

data(hello="world", number=123, another_number=456)

