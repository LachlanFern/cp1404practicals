import wikipedia


def main():
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)

            print(page.title)
            print(page.summary)
            print(page.url)

        except wikipedia.exceptions.DisambiguationError as options:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(options.options)

        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        print()
        title = input("Enter page title: ").strip()

    print("Thank you.")


main()
