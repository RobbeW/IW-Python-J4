def schuif_links(lijst, nummer):   
    newlist = []
    for i in range(len(lijst)):
        newlist.append(lijst[(i + nummer) % len(lijst)])
    return newlist