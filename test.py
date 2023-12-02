"""Testing the module"""

MODE = "CONSOLE" # "CONSOLE" | "IMAGE"

import pixelbattleConsole as pb

def main():
    while True:
        comand = input("Enter command: ").lower()

        match comand:
            case "set":
                if MODE == "IMAGE":
                    pb.SetPixel(
                        int(input("Enter x: ")), 
                        int(input("Enter y: ")),
                        (
                            int(input("Enter r: ")),
                            int(input("Enter g: ")),
                            int(input("Enter b: "))
                        )
                    )
                else:
                    pb.SetPixel(
                        int(input("Enter x: ")), 
                        int(input("Enter y: ")),
                        input("Color: ").upper(),
                    )
                pb.Show()
            case "show":
                pb.Show()
            case "download":
                if MODE == "IMAGE":
                    pb.Canvas.save(f"{input('Enter name: ')}.png")
                else:
                    print("Can't download image in console mode")
            case "clear":
                pb.ClearCanvas()
                pb.Show()
            case "exit":
                break
            case _:
                print("Unknown command \"{}\"".format(comand))

if __name__ == "__main__":
    main()