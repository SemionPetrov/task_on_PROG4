def gen_bin_tree(Root=3, height=3, L_branch=lambda x: x + 3, R_branch=lambda x: x + 2):
    if height == 0:
        return {'value': Root}
    else:
        left = gen_bin_tree(L_branch(Root), height - 1, L_branch, R_branch)
        right = gen_bin_tree(R_branch(Root), height - 1, L_branch, R_branch)
        return {'value': Root, 'left': left, 'right': right}


def pretty_print_spaced(tree, level=0):
    if not tree: return

    indent = "      " * level
    print(f"{indent}{tree['value']}")

    if 'right' in tree: print(); pretty_print_spaced(tree['right'], level + 1)

    if 'left' in tree: pretty_print_spaced(tree['left'], level + 1)

if __name__ == "__main__":
    print(pretty_print_spaced(gen_bin_tree(Root=5,height=6)))