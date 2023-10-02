import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='input.txt')
    parser.add_argument('--output', type=str, default='output.txt')
    parser.add_argument('--mode', type=str, default='c')
    parser.add_argument('--method', type=str, default="ari")
    args = parser.parse_args()

    if args.method == 'ari':
        from ari import compress_ari, decompress_ari

        if args.mode == 'c':
            compress_ari(args.input, args.output)
        elif args.mode == 'd':
            decompress_ari(args.input, args.output)
    elif args.method == 'ppm':
        from ppm import compress_ppm, decompress_ppm

        if args.mode == 'c':
            compress_ppm(args.input, args.output)
        elif args.mode == 'd':
            decompress_ppm(args.input, args.output)


if __name__ == '__main__':
    main()