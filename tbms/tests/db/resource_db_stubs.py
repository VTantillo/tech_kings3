def create(item, values):
    if item == 'reference material':
        if 'name' not in values or 'file_location' not in values or \
                'type' not in values:
            item_id = -1
        else:
            item_id = 1

    elif item == 'survey':
        if 'name' not in values or 'file_location' not in values or \
                'completed' not in values or 'user_id' not in values:
            item_id = -2
        else:
            item_id = 2

    else:
        item_id = -3

    return item_id

