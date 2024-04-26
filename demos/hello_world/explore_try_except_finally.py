def main() -> None:
    try:
        raise Exception("something went wrong")
    except Exception as exc:
        print(f"handle it! {exc}")


if __name__ == "__main__":
    main()
