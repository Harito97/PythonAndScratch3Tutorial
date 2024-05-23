def check_doi_xung(n: str):
    return n[::-1] == n


if __name__ == "__main__":
    n = int(input())

    while not check_doi_xung(str(n)):
        n += int(str(n)[::-1])

    print(n)
