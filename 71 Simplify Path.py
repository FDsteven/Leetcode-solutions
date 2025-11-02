def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    path_item_list = path.split("/")
    stack = []
    for i in range(1,len(path_item_list)):
        current = path_item_list[i]
        current = current.replace("/",'')
        if current == "..":
            if stack:
                stack.pop()
                continue
        if current != ".":
            stack.append(current)
    final_str = "/" + "/".join(stack)
    return final_str





path = "/home/"
path = "/home//foo/"
path = "/home/user/Documents/../Pictures"
print(simplifyPath(path))