def function(**kwargs):
    print(kwargs)
    print(kwargs["a"])


function(a=1, b=2, c=3)
