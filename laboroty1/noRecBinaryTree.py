def gen_bin_tree(Root = 3, height = 3, L_branch = lambda x: x+3,R_branch = lambda x: x+2 )-> dict:
    roots = [[Root]]
    for leaf in range(height):
        if (len(roots)==1):
            r =roots[0]
        else:
            r =[item for s in roots[-1]for item in s]
        leaves = list(map(lambda root_value:[L_branch(root_value),R_branch(root_value)],r))
        roots.append(leaves)
    roots.reverse()
    roots[-1] = [roots[-1]]
    roots[0] = list(map(lambda x:[{str([x]): []},
                                  {str(x[1]):[]}
                                  ], roots[0]))
    for i in range(height):
        sublist = roots[i]
        for j in range(len(sublist)):
            x = sublist.pop()
            roots[i+1][j//2][j%2] = {str(roots[i+1][j//2][j%2]):x}
    tree = roots[-1][0][0]
    return tree

def pretty_print_spaced(tree, level=0):
    if not tree: return

    indent = "      " * level
    print(f"{indent}{tree['value']}")

    if 'right' in tree: print(); pretty_print_spaced(tree['right'], level + 1)

    if 'left' in tree: pretty_print_spaced(tree['left'], level + 1)

if __name__ == "__main__":
    print(pretty_print_spaced(gen_bin_tree(Root=5,height=5)))