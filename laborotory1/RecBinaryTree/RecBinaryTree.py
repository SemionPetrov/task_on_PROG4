from laborotory1.exceptions_for_gen_bin_tree import *


def validate_input(Root, height):
    if not isinstance(Root, (int, float)):
        raise InvalidRootException(Root)
    if not isinstance(height, int) or height < 0:
        raise InvalidHeightException(height)

def gen_bin_tree(Root=17, height=4, L_branch=lambda x: (x - 4) ** 2, R_branch=lambda x: (x + 3) * 2):
    validate_input(Root, height)
    if height == 0:
        return {'value': Root, 'left': None, 'right': None}
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
    try:
        print(pretty_print_spaced(gen_bin_tree(Root=5,height=6)))
    except Exception as e:
        print(f"Error: {e}")