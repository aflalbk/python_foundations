def check_scope():
    def do_local():
        test = "this is do local"

    def do_non_local():
        nonlocal test
        test = "this is do non local"

    def do_global():
        global test
        test = "this is do global"

    test = "default test"
    do_local()
    print("what is the value of test after call do local : " + test)
    do_non_local()
    print("what is the value of test after call do non local : " + test)
    do_global()
    print("what is the value of test after call do global : " + test)


check_scope()
print("what is the value of test after call do global __main__ : " + test)

