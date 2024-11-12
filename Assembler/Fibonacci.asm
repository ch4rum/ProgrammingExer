.data
    number: .asciiz "�Cu�ntos n�meros de la serie Fibonacci desea generar (m�ximo 45)?"
    result: .asciiz "La serie Fibonacci es: "
    sume: .asciiz "La suma de los n�meros de la serie es: "
    commaSpace: .asciiz ", "
    newline: .asciiz "\n"

.text
main:
    # Pedir al usuario cu�ntos n�meros desea generar
    li $v0, 4            
    la $a0, number       
    syscall

    li $v0, 5            
    syscall
    move $t0, $v0        # guardar el n�mero de t�rminos en $t0

    # Verificar que el n�mero es positivo
    blez $t0, exit       

    # Inicializar variables para la serie Fibonacci
    li $t1, 0            # primer n�mero de la serie
    li $t2, 1            # segundo n�mero de la serie
    li $t3, 0            # �ndice actual
    li $t4, 0            # suma total de la serie
    li $t5, 0            # n�mero de t�rminos impresos

    # Imprimir el mensaje de la serie Fibonacci
    li $v0, 4            
    la $a0, result    # cargar la direcci�n del mensaje de serie
    syscall

print_series:
    # Imprimir el n�mero actual
    li $v0, 1            
    move $a0, $t1        # poner el n�mero actual en $a0
    syscall

    # Imprimir coma y espacio si no es el �ltimo n�mero
    bge $t5, $t0, end_series
    li $v0, 4            
    la $a0, commaSpace   # cargar la direcci�n de la coma y espacio
    syscall

    # Actualizar la suma
    add $t4, $t4, $t1    # agregar el n�mero actual a la suma

    # Preparar el siguiente n�mero de la serie
    add $t6, $t1, $t2    # siguiente n�mero es la suma de los dos anteriores
    move $t1, $t2        # actualizar $t1 para el siguiente n�mero
    move $t2, $t6        # actualizar $t2 para el siguiente n�mero

    # Incrementar el contador de n�meros impresos
    addi $t5, $t5, 1

    # Volver a imprimir la serie hasta alcanzar el n�mero deseado
    j print_series

end_series:
    # Imprimir salto de l�nea
    li $v0, 4            
    la $a0, newline      # cargar la direcci�n del salto de l�nea
    syscall

    # Imprimir el mensaje de la suma
    li $v0, 4            
    la $a0, sume       # cargar la direcci�n del mensaje de suma
    syscall

    # Imprimir la suma total
    li $v0, 1            
    move $a0, $t4        # poner la suma total en $a0
    syscall

    # Salto de l�nea despu�s de imprimir la suma
    li $v0, 4            
    la $a0, newline      # cargar la direcci�n del salto de l�nea
    syscall

exit:
    li $v0, 10           # syscall para exit
    syscall
