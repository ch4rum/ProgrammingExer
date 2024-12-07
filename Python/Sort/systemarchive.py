import colorama

class Archives:

    def open_archives(self: 'Archives', archive: str) -> list[int]:
        """
        Opens a file and reads the data it contains.

        Parameters:
        - File: Name of the file to open.

        Returns:
        - List of integers read from the file."""

        try:
            with open(archive,"r") as file:
                data = file.read().split()
                data = [int(_) for _ in data]
            if not data:
                print(f"[{colorama.Fore.LIGHTRED_EX}-{colorama.Style.RESET_ALL}] El archivo esta vacio")
            return data  
        except FileNotFoundError:
            print(f"[{colorama.Fore.LIGHTRED_EX}-{colorama.Style.RESET_ALL}] El archivo no fue encontrado")
        except ValueError:
            print(f"[{colorama.Fore.LIGHTRED_EX}-{colorama.Style.RESET_ALL}] Los datos en el archivo no son numeros enteros validos")

    def export_archive(self: 'Archives', argsname: str, sort_data: list[int]) -> None:
        """
        Exports the sorted data to a file.

        Parameters:
        - argsname: Name of the destination file.
        - sorted_data: List of sorted data."""

        with open(argsname,'w') as file:
            file.write('\n'.join(map(str,sort_data))+'\n')
        print(f"[{colorama.Fore.LIGHTGREEN_EX}+{colorama.Style.RESET_ALL}] Archivo exportado exitosamente {colorama.Fore.YELLOW}./{argsname}\n{colorama.Style.RESET_ALL}")    
