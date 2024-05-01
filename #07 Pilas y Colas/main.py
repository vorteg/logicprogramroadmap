"""
    Pilas y Colas
"""

#Pila/Stack (LIFO)

# stack = []
# # push
# stack.append("1")
# stack.append("2")
# stack.append("3")
# print(stack)
# # pop
# stack_item = stack[len(stack)-1]
# del stack[len(stack)-1]
# print(stack_item)
# print(stack)

# #Cola/ Queue (FIFO)

# queue = []

# # enqueue
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)

# # dequeue
# queue_item = queue[0]
# del queue[0]

# print(queue_item)
# print(queue)



def web_nav():
    web_pages = []
    while True:
        acction = input("Selecciona la tarea a realizar salir/adelante/atras o agrega una url \n")

        match acction:
            case "salir":
                break
            case "adelante":
                print("Navegando hacia adelante")
            case "atras":
                if len(web_pages) > 0:
                    web_pages.pop()
                    print("Navegando hacia atras")
            case _:
                web_pages.append(acction)
        
        print(web_pages[-1]) if len(web_pages) > 0 else print("Pagina de inicio")

            
web_nav()