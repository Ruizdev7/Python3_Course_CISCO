try:
    raise Exception
except :
    print("a")

except Exception :
    print("b")
except Exception :
    print("c")
