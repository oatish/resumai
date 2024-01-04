import os
from argparse import ArgumentParser
from resumai.resume import read_resume, Curator
from openai import OpenAI
from pprint import pprint


def main():
    argparser = ArgumentParser()
    argparser.add_argument("--file", "-f", type=str, default="resume.toml")
    argparser.add_argument("--token", "-t", type=str, default=os.environ["OPENAI_API_KEY"])
    argparser.add_argument("--job_posting", "-j", type=str, default="This is a job posting.")
    argparser.add_argument("--job_posting_file", "-J", type=str)
    argparser.add_argument("--output", "-o", type=str, default="")
    args = argparser.parse_args()

    resume = read_resume(args.file)
    client = OpenAI(api_key=args.token)
    job = ""
    if args.job_posting_file:
        with open(args.job_posting_file, "r") as f:
            job = f.read()
    curator = Curator(resume, client, job)
    new_resume = curator.curate()
    if len(args.output) > 0:
        new_resume.write(args.output)
    pprint(new_resume)


if __name__ == "__main__":
    main()
