def what_this_func_is_doing(inp1, inp2):
    ggg = {}
    for aaa in range(len(inp1)):
        ggg[inp1[aaa]] = aaa
    for bbbggd in range(len(inp1)):
        c = inp2 - inp1[bbbggd]
        if c in ggg and ggg[c] != bbbggd:
            return [bbbggd, ggg[c]]


if __name__ == '__main__':
    print(what_this_func_is_doing(inp1=[1, 2, 3], inp2=3))
    print(what_this_func_is_doing(inp1=[1, 2, 3, 4, 5, 6], inp2=10))
    print(what_this_func_is_doing(inp1=[1, 3, 5], inp2=2))
