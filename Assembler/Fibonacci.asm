.data
    number: .asciiz "¿Cuántos números de la serie Fibonacci desea generar (máximo 45)?"
    result: .asciiz "La serie Fibonacci es: "
    sume: .asciiz "La suma de los números de la serie es: "
    commaSpace: .asciiz ", "
    newline: .asciiz "\n"

.text
main:
    # Pedir al usuario cuántos números desea generar
    li $v0, 4            
    la $a0, number       
    syscall

    li $v0, 5            
    syscall
    move $t0, $v0        # guardar el número de términos en $t0

    # Verificar que el número es positivo
    blez $t0, exit       

    # Inicializar variables para la serie Fibonacci
    li $t1, 0            # primer número de la serie
    li $t2, 1            # segundo número de la serie
    li $t3, 0            # índice actual
    li $t4, 0            # suma total de la serie
    li $t5, 0            # número de términos impresos

    # Imprimir el mensaje de la serie Fibonacci
    li $v0, 4            
    la $a0, result    # cargar la dirección del mensaje de serie
    syscall

print_series:
    # Imprimir el número actual
    li $v0, 1            
    move $a0, $t1        # poner el número actual en $a0
    syscall

    # Imprimir coma y espacio si no es el último número
    bge $t5, $t0, end_series
    li $v0, 4            
    la $a0, commaSpace   # cargar la dirección de la coma y espacio
    syscall

    # Actualizar la suma
    add $t4, $t4, $t1    # agregar el número actual a la suma

    # Preparar el siguiente número de la serie
    add $t6, $t1, $t2    # siguiente número es la suma de los dos anteriores
    move $t1, $t2        # actualizar $t1 para el siguiente número
    move $t2, $t6        # actualizar $t2 para el siguiente número

    # Incrementar el contador de números impresos
    addi $t5, $t5, 1

    # Volver a imprimir la serie hasta alcanzar el número deseado
    j print_series

end_series:
    # Imprimir salto de línea
    li $v0, 4            
    la $a0, newline      # cargar la dirección del salto de línea
    syscall

    # Imprimir el mensaje de la suma
    li $v0, 4            
    la $a0, sume       # cargar la dirección del mensaje de suma
    syscall

    # Imprimir la suma total
    li $v0, 1            
    move $a0, $t4        # poner la suma total en $a0
    syscall

    # Salto de línea después de imprimir la suma
    li $v0, 4            
    la $a0, newline      # cargar la dirección del salto de línea
    syscall

exit:
    li $v0, 10           # syscall para exit
    syscall
