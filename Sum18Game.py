import random
if __name__ == "__main__":
    while True:
        print "Use these numers plus any operators and paranthesis to make 18"
        for i in range(6):
            print " \t"  + str(random.randint(1,20))

        response = raw_input("Type 'stop' to finish:")
        if response.lower() == 'stop':
            exit(1)
    pass
