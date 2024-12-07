import colorama
from pwn import *

class SortAlg:
    
    def __init__(self: 'SortAlg'):
        self.__autor__ = "Ch4rum"
        self.__copyright__ = "Copyright © 2024 Ch4rum -> https://www.instagram.com/ch4rum/"
        self.__version__ = "Version 1.1"
        self.__maintainer__ = "Ch4rum"

    def banner(self: 'SortAlg'):
        print(f"""{colorama.Fore.GREEN}                                                    
                  :                                        
           .     t#,                                       
          ;W    ;##W.   j.                                 
         f#E   :#L:WE   EW,       GEEEEEEEL :;;;;;;;;;;;;;.
       .E#f   .KG  ,#D  E##j      ,;;L#K;;.  jWWWWWWWW###L 
      iWW;    EE    ;#f E###D.       t#E             ,W#f  
     L##Lffi f#.     t#iE#jG#W;      t#E            ,##f   
    tLLG##L  :#G     GK E#t t##f     t#E           i##j    
      ,W#i    ;#L   LW. E#t  :K#E:   t#E          i##t     
     j#E.      t#f f#:  E#KDDDD###i  t#E         t##t      
   .D#j         f#D#;   E#f,t#Wi,,,  t#E        t##i       
  ,WK,           G#t    E#t  ;#W:    t#E       j##;        
  EG.             t     DWi   ,KK:    fE      :##,         
  ,                                    :      ,W,          
                                              :: {colorama.Style.RESET_ALL}{colorama.Fore.BLUE}v{self.__version__.split()[1]}{colorama.Style.RESET_ALL}
    \n\t{colorama.Fore.RED}{self.__copyright__}{colorama.Style.RESET_ALL}""")

    def bubble_sort(self: 'SortAlg', numbers: list[int], p1: log.progress) -> list[int]:
        """
        Implements the Bubble sorting algorithm,the Bubble sorting algorithm compares 
        pairs of adjacent elements in the list and swaps them if they are in the wrong order.
        This is repeated until no more swaps are necessary, indicating that the list is sorted.

        Complexity:
        - Worst case: O(n^2), where n is the number of elements in the list.

        Parameters:
        - Numbers: List of numbers to be sorted.
        - p1: Progress log object.

        Returns:
        - List of sorted numbers."""

        for i in range(len(numbers)): #1
            p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}BubbleSort {colorama.Style.RESET_ALL}- Elemento -> [{colorama.Fore.RED}{numbers[i]}{colorama.Style.RESET_ALL}]")
            for j in range(len(numbers)-i-1): #3
                if (numbers[j] > numbers[j+1]): #4
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j] #7         
        return numbers # 1
    
    def selection_sort(self: 'SortAlg', numbers: list[int], p1: log.progress) -> list[int]:
        """
        It implements the Sort by Selection algorithm.The Sort by Selection algorithm 
        algorithm looks for the smallest element in the list and places it in the correct position.
        This is repeated for all the elements in the list, dividing the list into two parts: the sorted part and the unsorted part. 
        parts: the sorted part and the unsorted part.

        Complexity:
        - Worst case: O(n^2), where n is the number of elements in the list.

        Parameters:
        - Numbers: List of numbers to be sorted.
        - p1: Progress log object.

        Returns:
        - List of sorted numbers."""
        
        for i in range(len(numbers)):#1
            p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}SelectionSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[i]}{colorama.Style.RESET_ALL}]")
            mini = i #1
            for j in range(i+1,len(numbers)):#2
                if (numbers[j] < numbers[mini]): #3
                    mini = j #1
            numbers[i], numbers[mini] = numbers[mini], numbers[i] #5
        return numbers #1
    
    def insertion_sort(self: 'SortAlg', numbers: list[int], p1: log.progress) -> list[int]:
        """
        Implements the insertion sort algorithm.The insertion sort algorithm builds a one-by-one sorted list by inserting the unsorted items in the correct position. 
        builds a one-by-one sorted list, inserting the unsorted elements in the correct position.
        At each iteration, it takes an unsorted element, compares it with the sorted elements and inserts it in the correct position. 
        inserts it in the correct position.

        Complexity:
        - Worst case: O(n^2), where n is the number of elements in the list.

        Parameters:
        - Numbers: List of numbers to sort.
        - p1: Progress log object.

        Returns:
        - List of sorted numbers."""
        
        for _ in range(len(numbers)): #1
            p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}InsertionSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[_]}{colorama.Style.RESET_ALL}]")
            pos = _#1
            aux = numbers[_] #2
            while ((pos>0) and (numbers[pos-1] > aux)): #4
                numbers[pos] = numbers[pos-1]#3
                pos -= 1#2
            numbers[pos] = aux#2
        return numbers#1

    def mergeSort(self: 'SortAlg', numbers: list[int], p1: log.progress) -> list[int]:
        """
        Implements the Merge Sort algorithm. The Merge Sort algorithm uses the “divide and conquer” strategy to divide the list into smaller halves.
        The “divide and conquer” strategy is used to divide the list into smaller halves,
        sort them, and then combine them into a larger sorted list.

        Complexity:
        - Worst case: O(n log n), where n is the number of elements in the list.

        Parameters:
        - Numbers: List of numbers to be sorted.
        - p1: Progress log object.

        Returns:
        - List of sorted numbers."""
        
        if len(numbers) > 1:#2
            mid = len(numbers)//2 #3
            L=numbers[:mid]#2
            R=numbers[mid:]#2
            self.mergeSort(L,p1)
            self.mergeSort(R,p1)
            i = j = k = 0 #3
            while i<len(L) and j < len(R):#5
                if L[i] <= R[j]: #3
                    numbers[k] =L[i]#3
                    i += 1#2
                else: 
                    numbers[k] = R[j]#3
                    j += 1#2
                k += 1#2
                p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}MergeSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[k-1]}{colorama.Style.RESET_ALL}]")
            while i < len(L):#2
                numbers[k] = L[i]#3
                i +=1 ; k += 1 #4
                p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}MergeSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[k-1]}{colorama.Style.RESET_ALL}]")
            while j < len(R):#2
                numbers[k] = R[j]#3
                j += 1; k += 1#4
                p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}MergeSort{colorama.Style.RESET_ALL} - Elemento -> [{colorama.Fore.RED}{numbers[k-1]}{colorama.Style.RESET_ALL}]")
        return numbers#1

    def quickSort(self: 'SortAlg', numbers: list[int], p1: log.progress) -> list[int]:
        """
        The Quick Sort algorithm uses a divide-and-conquer strategy to divide the list into smaller sublists.
        The Quick Sort algorithm uses a divide-and-conquer strategy to divide the list into smaller sublists,
        sort them and combine them into a sorted list. It uses a technique called partitioning to choose 
        an item as a pivot and rearrange the list so that items smaller than the pivot are on the left and items larger than the pivot are on the right. 
        are on the left and those larger than the pivot are on the right.

        Complexity:
        - Mean and expected case: O(n log n), where n is the number of elements in the list.
        - Worst case: O(n^2), but rarely occurs in practice due to intelligent choice of efficient pivots and partitions. 
        efficient pivots and partitions.
        
        Parameters:
        - Numbers: List of numbers to sort.
        - p1: Progress log object.

        Returns:
        - List of sorted numbers."""

        return self._quickSortHelp(numbers,0,len(numbers)-1)

    def _partition(self: 'SortAlg', numbers: list[int], low: int, high: int) -> int:

            pivot = numbers[high] #2
            i = low - 1 #2
            for _ in range(low,high): #1
                if numbers[_] <= pivot: #2
                    i += 1 #2
                    numbers[i], numbers[_] = numbers[_], numbers[i] #5
                    p1.status(f"{colorama.Fore.LIGHTYELLOW_EX}QuickSort{colorama.Style.RESET_ALL} - Elemento [{colorama.Fore.RED}{numbers[_]}{colorama.Style.RESET_ALL}]")
            numbers[i+1], numbers[high] = numbers[high], numbers[i+1] #5
            return i+1 #2
        
    def _quickSortHelp(self: '', numbers: list[int], low: int, high: int) -> list[int]:

            if low < high: #1
                pi = self._partition(numbers,low,high)
                self._quickSortHelp(numbers,low,pi-1)
                self._quickSortHelp(numbers,pi+1,high)
            return numbers
        
