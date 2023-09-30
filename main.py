from argparse import ArgumentParser
from argparse import Namespace

def get_args() -> Namespace:
    """
    Get arguments from command line.

    :return: Object containing argument values.
    """
    parser = ArgumentParser()
    parser.add_argument("--image_path", type=str, default="resources/img1.jpg")
    return parser.parse_args()

def main() -> None:
    """
    Main method.

    :return: None
    """
    args = get_args()
    img_path = args.image_path
    print(img_path)

if __name__ == '__main__':
    main()
