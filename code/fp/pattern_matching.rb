foo = [1, 2.4, 3.1]
case foo
    in [1, 2, 3]
        puts("it's a list with 1, 2, and 3")
    in [1, 2, _]
        puts("it's a list with 1, 2, and whatever")
    in [1, Float, Float]
        puts("it's a list with 1, and two floats")
    else
        "not matched"
end
