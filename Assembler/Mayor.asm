.data
    range: .asciiz "Cuantos números desea comparar (entre 3 y 5)?"
    number: .asciiz "Ingrese el número "
    result: .asciiz "El número mayor es: "
    newline: .asciiz "\n"

.text
main:
    # Pedir al usuario cuantos números desea comparar
    li $v0, 4            
    la $a0, range      
    syscall
 
    li $v0, 5            
    syscall
    move $t0, $v0        

    # Verificar que el número está entre el intervalo de 3 y 5.
    li $t1, 3            
    blt $t0, $t1, exit   
    li $t1, 5            
    bgt $t0, $t1, exit   

    # Leer los números
    li $t1, 0            
    li $t2, -2147483648  

read_numbers:
    li $v0, 4            
    la $a0, number      
    syscall

    li $v0, 5            
    syscall
    move $t3, $v0        

    # Comparar con el máximo actual
    bgt $t3, $t2, update_max
    j check_next

update_max:
    # actualizar el máximo
    move $t2, $t3        

check_next:    
    addi $t1, $t1, 1   		# incrementar el indice      
    blt $t1, $t0, read_numbers	# si aún hay números por leer, repetir

    # Mostrar el resultado
    li $v0, 4            
    la $a0, result    
    syscall

    move $a0, $t2        
    li $v0, 1            
    syscall

    # Salto de línea
    li $v0, 4            
    la $a0, newline      
    syscall

exit:
    li $v0, 10           
    syscall
