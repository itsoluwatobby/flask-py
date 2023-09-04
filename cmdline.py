
def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Halo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == "__main__":
    import argparse
    # import sys
    # args = sys.argv[1:]
    # [print(x, end=' ') for x in args]

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )
    # dest="firstName",
    parser.add_argument(
        "-n", "--name", metavar="name", required=True,
        help="The name of the person to greet"
    )
    parser.add_argument(
        "-l", "--lang", metavar="language", required=True,
        help="The language of the greeting", choices=["English", "Spanish", "German"]
    )

    args = parser.parse_args()
    hello(args.name, args.lang)
