def delete(item, item_id):
    n = 25
    if item_id < 0:
        return False
    if item_id > n:
        return False

    if item != "user" and item != "credentials":
        return False

    return True
