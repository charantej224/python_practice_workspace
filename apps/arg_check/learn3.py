import argparse

my_parser = argparse.ArgumentParser(prog='learn3',
                                    description='List the content of a folder')

my_parser.add_argument('--path', action='store', type=int, required=False, default=120)

# Execute parse_args()
args = my_parser.parse_args()

print(args)
