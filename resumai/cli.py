from argparse import ArgumentParser
from resumai.resume import read_resume


def main():
    argparser = ArgumentParser()
    argparser.add_argument("--file", "-f", type=str, default="resume.toml")
    args = argparser.parse_args()

    read_resume(args.file)


if __name__ == '__main__':
    main()
