def maxMin(operations, x):

    push_pop = list()
    elements = list()
    product = list()

    for op in operations:
        try:
            if op == 'push' or op == 'pop':
                push_pop.append(op)

        except NotValidMethod as error:
            print(error)
    
    for method,element in zip(push_pop, x):
        if method == 'push':
            elements.append(element)
            product_push = max(elements)*min(elements)
            product.append(product_push)
        else :
            element_index = elements.index(element)
            elements.pop(element_index)
            product_pop = max(elements)*min(elements)
            product.append(product_pop)

    return product


operation = ['push','push', 'push', 'pop']
x = [1, 2, 3, 1]

print(maxMin(operation, x))